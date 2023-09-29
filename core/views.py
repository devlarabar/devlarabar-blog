from django.shortcuts import render


def index(request):
    context = {
        'title': None,
        'theme': 'dark'
    }
    return render(request, 'core/index.html', context)
