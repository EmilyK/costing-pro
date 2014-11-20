from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse
from forms import BusinessProfileForm
from django.core.context_processors import csrf


def home(request):
	if request.user.is_authenticated():
		return redirect('business_profile')
	else:
		return render_to_response('dashboard/home.html', 
								  {}, 
								  RequestContext(request))


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
