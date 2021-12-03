from django.shortcuts import render

def Ingreso(request):
	return render(request, 'ingreso/ingreso.html')
