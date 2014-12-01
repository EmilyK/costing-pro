import user
from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse, get_object_or_404
from forms import BusinessProfileForm, UserSignUpForm, RawmaterialForm
from models import RawMaterial
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf, request
from django.contrib.auth import authenticate, login


def home(request):
    return render_to_response('dashboard/home.html',
            {},
                                  RequestContext(request))

def  signup(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)

        if form.is_valid():
            user = form.save()

            user.set_password(user.password)
            user.save()

            profile = form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print form.errors

    else:
        form = UserSignUpForm()

    return render_to_response(
            'dashboard/signup.html',
            {'form': form, 'registered': registered},
            context)

def login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return RediectView(url='/dashboard/business_profile.html')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('registration/login.html', {}, context)
    
def business_profile(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)

        if form.is_valid():

            form.save()

            return menu(request)

        else:
            print form.errors
            c['form'] = form

    else:
        form = BusinessProfileForm()
        c['form'] = form

    return render_to_response('dashboard/business_profile.html', c)

def menu(request):
    return render_to_response('dashboard/menu.html',
        {},
                              RequestContext(request))


def costing(request):
    form = RawmaterialForm()

    if request.method == 'POST':
        form = RawmaterialForm(request.POST)

        if form.is_valid():

            raw_material = form.save()

            return redirect('costing_detail', pk=raw_material.pk)

        else:
            pass

    return render_to_response('dashboard/costing.html',
        {'form': form},
        RequestContext(request)
        )
    
def costing_detail(request, pk):
    raw_material = get_object_or_404(RawMaterial, pk=pk)

    return render_to_response('dashboard/costing_detail.html',
            {},
                                  RequestContext(request))

def costing_raw_materials(request, pk):
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    if request.user.is_authenticated:
        raw_materials = RawMaterial.objects.filter(user=request.user)
    else:
        raw_materials = None
    return render_to_response('dashboard/costing_raw_materials.html',
                              {'raw_materials': raw_materials}, 
                              RequestContext(request))