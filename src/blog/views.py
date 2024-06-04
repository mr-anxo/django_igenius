from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, "blog.html")

def article(request, numero_article):
    if 1 <= numero_article <= 3:
        return render(request, f"article{numero_article}.html")
    else:
        return render(request, "404.html")