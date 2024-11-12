from django.shortcuts import render


def blogs_home(request):
    template_name = 'blog/index.html'
    return render(request, template_name)


def articles(request):
    template_name='blog/articles_home.html'
    return render(request, template_name)


def blog_post(request):
    template_name='blog/index.html'
    return render(request, template_name)