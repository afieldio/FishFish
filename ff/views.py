from django.shortcuts import render

def events(request):
	user = request.user
	context = {'user':user}
	return render(request, 'events.html', context)