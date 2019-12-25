from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html', {})
def catalog(request):
    return render(request, 'catalog/catalog.html', {})  
def videocard(request):
    return render(request, 'videocard/videocard.html', {})  
