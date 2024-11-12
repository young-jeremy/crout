from django.shortcuts import render


def home_page(request):
    template_name = 'home_index.html'
    return render(request, template_name)


def juice_haven(request):
    template_name = 'home/juice_haven.html'
    return render(request, template_name)


def contact(request):
    template_name='home/contact.html'
    return render(request, template_name)

def about(request):
    template_name='home/about.html'
    return render(request, template_name)


def pricing(request):
    template_name='home/pricing.html'
    return render(request, template_name)


def frequently_asked_questions(request):
    template_name='home/faq.html'



    return render(request, template_name, {'about':about })


def portfolio(request):
    template_name = 'home/portfolio.html'
    return render(request, template_name)

def privacy(request):
    template_name='home/privacy.html'
    return render(request, template_name)


def terms_and_conditions(request):
    template_name='home/terms_and_conditions.html'
    return render(request, template_name)


def portfolio_overview(request):
    template_name = 'home/portfolio-overview.html'
    return render(request, template_name)


def portfolio_item(request):
    template_name = 'home/portfolio-item.html'
    return render(request, template_name)


def blog_post(request):
    template_name = 'home/blog-post.html'
    return render(request, template_name)


def blog_home(request):
    template_name = 'home/blog-home.html'
    return render(request, template_name)


def learn_more(request):
    template_name='home/learn_more.html'
    return render(request, template_name)

