import user
from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse, get_object_or_404
from forms import BusinessProfileForm, UserSignUpForm, UserLoginForm, RawmaterialForm
from models import RawMaterial
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf, request


def home(request):
    return render_to_response('dashboard/home.html',
            {},
                                  RequestContext(request))


def signup(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():

            form.save()

            return login(request)

        else:
            print form.errors
            c['form'] = form


    else:
        form = UserSignUpForm()
        c['form'] = form

    return render_to_response('dashboard/signup.html', c)


def login(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():

            form.save()

            return menu(request)

        else:
            print form.errors
            c['form'] = form


    else:
        form = UserLoginForm()
        c['form'] = form

    return render_to_response('dashboard/login.html', c)

def auth_view(request):
    eamil = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(eamil=eamil, password=password)

    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/business_profile')
    else:
        return HttpResponseRedirect('/signup')


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

    # {'form': form}


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
