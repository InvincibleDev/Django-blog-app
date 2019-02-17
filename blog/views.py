from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

def home(request):
    all_post= Post.objects.all()
    return render(request,"home.html",{'all_post':all_post})


def about(request,name):
    return render(request, "about.html", {'person':name})

def create_post(request):

    if request.method == "POST":
        return HttpResponse(request.POST['tittle'])

    return render(request, "create.html")
