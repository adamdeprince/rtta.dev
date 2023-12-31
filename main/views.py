from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/index.html')

def install(request):
    return render(request, 'main/install.html')

def overview(request):
    return render(request, "main/overview.html")
