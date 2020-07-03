from django.shortcuts import render
from .models import blogPost
from django.http import HttpResponse
# Create your views here.
def index(request):
    mypost = blogPost.objects.all()
    print(mypost)
    return render(request, 'blog/index.html', {'mypost':mypost})

def blogpost(request, id):
    post = blogPost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post':post})
