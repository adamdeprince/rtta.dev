from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def install(request):
    return render(request, 'install.html')

def overview(request):
    return render(request, "overview.html")
