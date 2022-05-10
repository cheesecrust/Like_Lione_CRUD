from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from .form import BlogForm
from django.core.paginator import Paginator


def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    pagnum = request.GET.get('page')
    blogs = paginator.get_page(pagnum)
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    # return render(request, 'new.html')
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form': form})


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.contents = request.POST['contents']
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)


def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk=id)  # 파라미터 id를 받아서 디비에 해당 객체를 가져온다.
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, id):
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST['title']
    update_blog.contents = request.POST['contents']
    update_blog.save()
    return redirect('detail', update_blog.id)


def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect('home')


def search(request):
    search_title = request.POST['title']
    search_blog = get_object_or_404(Blog, title=search_title)
    return redirect('detail', search_blog.id)


def like(request, id):
    like_blog = get_object_or_404(Blog, pk=id)
    like_blog.likes += 1
    like_blog.save()
    return redirect('detail', like_blog.id)
