from django.shortcuts import render


def index(request):

    readme = open('README.md').read()
    return render(request, 'index.html', {'readme': readme})


def about(request):
    return render(request, 'about.html')
