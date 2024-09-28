from django.shortcuts import render


# Create your views here.
def about_pages(request):
    return render(request, 'about/about.html')
