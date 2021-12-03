from django.shortcuts import render

def Ods(request):
	return render(request, 'ods/ods.html')