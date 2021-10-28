from django.shortcuts import redirect, render
from . models import Blogs, Comment, category
from django.db.models import Count
# Create your views here.

def blogs(request):
    blog = Blogs.objects.all()
    return render(request,'blogs/blogs.html',{'blog':blog})

def categoryblog(request,slug):
    res= {}
    res['blog'] = Blogs.objects.filter(category__slug=slug)
    return render(request,'blogs/blogs.html',res)
def singleblog(request,slug1):
    res = {}
    res['blog'] = Blogs.objects.get(slug=slug1)
    res['recentblog'] = Blogs.objects.all().order_by('date')
    res['cats'] = category.objects.all().annotate(num_posts=Count('Blogs')).order_by('-num_posts')
    return render(request,'blogs/singleblog.html',res)

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