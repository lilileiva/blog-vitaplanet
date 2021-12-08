from django.shortcuts import render

def Productos(request):

	#consulta para traer todos los productos
	p = Productos.objects.all()
	#contexto
	ctx = {}
	ctx['product'] = p
	ctx['titulo'] = "HOLA SOY EL TITULO"

	return render(request, 'productos/productos.html', ctx)

#en realidad en el template voy a tener variables separadas

#product que contiene los productos p