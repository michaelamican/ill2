from django.shortcuts import render, redirect
from django.template.loader import render_to_string

# Create your views here.
def index(request):
	return render(request,'index.html')

def interiors(request):
	return render(request,'interiors.html')

def leather(request):
	return render(request, 'leather.html')

def auto(request):
	return render(request,'auto.html')

def emboss(request):
	return render(request,'leathers/emboss.html')

def embossed(request, thing):
	return render(request, 'leathers/embossed/'+thing+'.html')

def plain(request):
	return render(request,'leathers/plain.html')

def plains(request, thing):
	return render(request,'leathers/plain/'+thing+'.html')

def tile(request):
	return render(request,'leathers/tile.html')

def tiles(request, thing):
	return render(request,'leathers/tile/'+thing+'.html')

def metalglass(request):
	return render(request, 'leathers/metalglass.html')

def metalglasses(request, thing):
	return render(request, 'leathers/metalglass/'+thing+'.html')

def mailing(request):
	return render(request,'mailing.html')

def shop(request):
	return render(request, 'shop.html')

def contact(request):
	return render(request,'contact.html')

def autos(request, car):
	return render(request, 'autos/'+car+'.html')

def admin(request):
	return render(request, 'admin.html')

def product(request):
	return render(request,'products.html')

def color(request):
	return render(request, 'CMF/overview.html')

def stories(request):
	return render(request, 'CMF/colors.html')

def showrooms(request):
	return render(request, 'showrooms.html')

def press(request):
	return render(request, 'press.html')

def pressed(request, thing):
	return render(request, 'press/'+thing+'.html')

def media(request):
	return render(request, 'insta.html')



