from django.shortcuts import render

# Create your views here.
def about1(request):
    return render(request, "about.html")