from django.shortcuts import redirect, render
from . models import Blogs, Comment

# Create your views here.

def blogs(request):
    blog = Blogs.objects.all()
    return render(request,'blogs/blogs.html',{'blog':blog})


def singleblog(request,slug1):
    blog = Blogs.objects.get(slug=slug1)
    return render(request,'blogs/singleblog.html',{'blog':blog})

def postcomment(request):
    if request.method == 'POST':
        blogid=request.POST.get("blogid")
        blog = Blogs.objects.get(pk=blogid)
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        body = request.POST['body']

        data = Comment(blog=blog,name=name,email=email,website=website,body=body)
        data.save()
    return redirect(f"/singleblog/{blog.slug}")