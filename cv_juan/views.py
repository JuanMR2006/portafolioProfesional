from django.shortcuts import render

def inicio(request):
    return render(request, 'cv_juan/index.html')