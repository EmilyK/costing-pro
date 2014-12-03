from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse, get_object_or_404
from forms import BusinessProfileForm, UserSignUpForm, RawmaterialForm, LoginForm
from models import RawMaterial, BusinessProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from django.core.context_processors import csrf, request
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db.models import Sum


def home(request):
    if request.user.is_authenticated():
        if BusinessProfile.objects.filter(user=request.user).exists():
            return redirect('business_profiles')
        return redirect('business_profile_new')
    return render_to_response('dashboard/home.html', {},
                              RequestContext(request))

def  signup(request):
    registered = False

    form = UserSignUpForm()

    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print form.errors

    return render_to_response(
            'dashboard/signup.html',
            {'form': form, 'registered': registered},
            RequestContext(request))

def _login(request):
    form = LoginForm() 
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        
            user = authenticate(username=username, password=password)
        
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('menu')
                else:
                    return HttpResponse("Your account is disabled.")
            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('registration/login.html', {'form': form},
         RequestContext(request))
    

def business_profile_list(request):
    if request.user.is_authenticated():
        business_profiles = BusinessProfile.objects.filter(user=request.user)
        if business_profiles.exists():

            return render_to_response('dashboard/business_profile_list.html',
            {'business_profiles': business_profiles}, RequestContext(request))
        else:
            messages.add_message(request, messages.INFO, "Please create a new business profile first")
            return redirect('business_profile_new')
    else:
        return HttpResponse("You need to login first!")


def business_profile(request):
    form = BusinessProfileForm()
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)
        if form.is_valid():
            business_profile = form.save()
            if request.user.is_authenticated():                
                # attribute user to business profile because of FK
                business_profile.user = request.user
                business_profile.save()

                return redirect('business_profiles')

        else:
            print form.errors

    return render_to_response('dashboard/business_profile.html', 
                              {'form': form, 'messages': messages.get_messages(request)}, 
                              RequestContext(request))

def menu(request):
    return render_to_response('dashboard/menu.html',{},
                              RequestContext(request))


def new_inventory(request, pk):
    form = RawmaterialForm()

    business_profile = get_object_or_404(BusinessProfile, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated():
        form = RawmaterialForm(request.POST)

        if form.is_valid():

            raw_material = form.save()
            # attribute raw material to "business profile"
            raw_material.business_profile = business_profile
            raw_material.save()

            return redirect('costing_raw_materials', pk=pk) #, id=raw_material.id)

        else:
            # TODO -> hande errors here!
            pass

    return render_to_response('dashboard/costing.html',
        {'form': form},
        RequestContext(request)
        )
    
def costing_detail(request, pk, id):
    # TODO -> change name of function to `raw_material`
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    raw_material = business_profile.rawmaterial_set.get(id=id)

    return render_to_response('dashboard/costing_detail.html',
            {},
                                  RequestContext(request))

def costing_raw_materials(request, pk):
    # TODO -> remove `all()` from below
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    total = 0.0

    if request.user.is_authenticated():
        raw_materials = RawMaterial.objects.filter(business_profile=business_profile)
        # raw_materials = RawMaterial.objects.all()
        total = raw_materials.aggregate(Sum('cost'))['cost__sum']
    else:
        raw_materials = None
    return render_to_response('dashboard/costing_raw_materials.html',
                              {'raw_materials': raw_materials, 'total': total}, 
                              RequestContext(request))