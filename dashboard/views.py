from django.shortcuts import RequestContext, render_to_response


def home(request):
	if request.user and request.user.is_authenticated():
		return redirect("business_profile") # it has to exist..otherwise error
	else:
		return render_to_response('dashboard/home.html', 
								  {}, 
								  RequestContext(request))
