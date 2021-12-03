from django.shortcuts import render

def Buscar(request):
	return render(request, 'buscar/buscar.html')
