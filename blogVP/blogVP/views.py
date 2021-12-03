from django.shortcuts import render

def Principal(request):
	return render(request, 'principal.html')
