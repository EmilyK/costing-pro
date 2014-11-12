from django.shortcuts import RequestContext, render_to_response


def home(request):
	return render_to_response('dashboard/home.html', 
		{}, 
		RequestContext(request))
