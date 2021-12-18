from django.shortcuts import render

def Principal(request):
	return render(request, 'principal.html')

def Perfil(request):
	args = {'user': request.user}
	return render(request, 'usuarios/perfil.html', args)