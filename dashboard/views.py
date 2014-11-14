from django.shortcuts import RequestContext, render_to_response, redirect, HttpResponse


def home(request):
	if request.user.is_authenticated():
		return redirect('business_profile')
	else:
		return render_to_response('dashboard/home.html', 
								  {}, 
								  RequestContext(request))


def business_profile(request):
	return render_to_response('dashboard/business_profile.html',
		{},
		RequestContext(request)
		)
		
