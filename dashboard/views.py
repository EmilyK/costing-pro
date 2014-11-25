import user
from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse
from forms import BusinessProfileForm, UserSignUpForm, UserLoginForm
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
    form = UserLoginForm(request.POST)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect('/business_profile')
    else:
    	return render_to_response('dashboard/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

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
