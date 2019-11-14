from django.shortcuts import render, redirect
from website.form import FormCliente
from website.models import Cliente


# Create your views here.

def home(request):
	return render(request, 'index.html')


def cliente(request):
        form = FormCliente(request.POST or None)
        if form.is_valid():
                form.save()
                return redirect('url_principal')
        else:
                return render(request, 'form_cliente.html' , {'form':form} )


def lista(request):
      objetos = Cliente.objects.all()
      return render(request,  'lista_cliente.html' , {'clientes': objetos})

