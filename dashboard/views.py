from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse, get_object_or_404
from forms import BusinessProfileForm, UserSignUpForm, RawmaterialForm, LoginForm, ProductForm, ProductRawMaterialForm
from models import RawMaterial, BusinessProfile, Product, ProductRawMaterial
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
    
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfileForm()

    args['form'] = form
    return render_to_response('registration/update_profile.html', args)

def update_profile_success(request):
    return render_to_response('registration/update_profile_success.html',{'fullname':request.user.username},
                              RequestContext(request))


def business_profile_list(request):
    if request.user.is_authenticated():
        business_profiles = BusinessProfile.objects.filter(user=request.user)
        if business_profiles.exists():
            return render_to_response('dashboard/business_profile_list.html',
            {'fullname':request.user.username, 'business_profiles': business_profiles}, RequestContext(request))
        else:
            messages.add_message(request, messages.INFO, "Please create a new business profile first")
            return redirect('business_profile_new')
    else:
        return HttpResponse("You need to login first!")

def business_profile_detail(request, pk):
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    return render_to_response('dashboard/business_profile_detail.html',
        {'business_profile': business_profile}, RequestContext(request))

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
                              {'fullname':request.user.username, 'form': form, 'messages': messages.get_messages(request)}, 
                              RequestContext(request))

def menu(request):
    return render_to_response('dashboard/menu.html',{'fullname':request.user.username},
                              RequestContext(request))


def all_products(request):
    return render_to_response('dashboard/all_products.html',
                              {'products': Product.objects.all()},
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
            # TODO -> handle errors here!
            pass

    return render_to_response('dashboard/costing.html',
        {'fullname':request.user.username, 'form': form},
        RequestContext(request)
        )

def new_product(request, pk):
    form = ProductForm()

    business_profile = get_object_or_404(BusinessProfile, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated():
        form = ProductForm(request.POST)

        if form.is_valid():

            product = form.save()
            # attribute "business profile" to product
            product.business_profile = business_profile
            product.save()

            messages.add_message(request, messages.INFO,
                "You've created a product successfully. Please add raw materials used.")

            return redirect('product_add_raw_material', pk=pk, id=product.id) #, id=product.id)

        else:
            # TODO -> handel errors here!
            pass

    return render_to_response('dashboard/new_product.html',
        {'form': form},
        RequestContext(request)
        )


def product(request, pk, id):
    _product = get_object_or_404(Product, id=id)
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    product_rawmaterials = _product.productrawmaterial_set.all()
    return render_to_response('dashboard/product.html', {'product': _product, 
        'product_rawmaterials': product_rawmaterials, 'business_profile': business_profile}, 
                                RequestContext(request))

def product_add_raw_material(request, pk, id):
    product = get_object_or_404(Product, id=id)
    business_profile = get_object_or_404(BusinessProfile, pk=pk)

    form = ProductRawMaterialForm(business_profile)

    user = request.user

    if business_profile.user == user and user.is_authenticated():
        if request.method == "POST":
            form = ProductRawMaterialForm(business_profile, request.POST)
            if form.is_valid():
                
                raw_material = get_object_or_404(RawMaterial, id=form.cleaned_data['raw_material']) #TODO
                amount = int(form.cleaned_data['amount'])
                
                if amount > raw_material.size or amount <= 0:
                    messages.add_message(request, messages.ERROR,
                        "The amount cannot be greater than your inventory. Current size is {0}".format(raw_material.size))
                else:
                    product_raw_material = ProductRawMaterial.objects.create(
                        raw_material = raw_material,
                        product = product,
                        business_profile = business_profile,
                        amount = amount)
                    product_raw_material.save()
                    # reduce inventory
                    raw_material.size -= amount
                    raw_material.save()
                    if product.created:
                        messages.add_message(request, messages.INFO, 
                            "You've updated your raw materials")
                    else:
                        product.created = True
                        product.save()
                        messages.add_message(request, messages.INFO,
                            "You've successfully created your product")
                    return redirect("product", pk=business_profile.pk, id=product.id )

            else:
                messages.add_message(request, messages.INFO, 
                    "The form input is invalid!")
        else:
            pass
    else:
        messages.add_message(request, messages.INFO, 
                             "You are forbidden from adding raw materials")
    return render_to_response('dashboard/add_raw_material_to_product.html',
                              {'form': form, 'messages': messages.get_messages(request)}, RequestContext(request))


def products(request, pk):
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    products = ProductRawMaterial.objects.filter(business_profile=business_profile)
    return render_to_response('dashboard/business_profile_product_list.html',
                              {'products': products},
                              RequestContext(request))


def costing_detail(request, pk, id):
    # TODO -> change name of function to `raw_material`
    business_profile = get_object_or_404(BusinessProfile, pk=pk)
    raw_material = business_profile.rawmaterial_set.get(id=id)

    return render_to_response('dashboard/costing_detail.html',
            {'fullname':request.user.username},
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
                              {'fullname':request.user.username, 'raw_materials': raw_materials, 'total': total}, 
                              RequestContext(request))