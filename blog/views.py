from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category

def home(request):
    # load all the post from database pagination with 10 per page
    posts = Post.objects.all()[:11]
    
    # load all the category from database 
    cats = Category.objects.all()

    postData = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request,'home.html',postData)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,"post.html",{'post': post,'cats':cats})

def category(request,url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat': cat, 'post':post})
