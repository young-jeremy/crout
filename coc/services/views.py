from django.shortcuts import render


def services(request):
    template_name ='services/services.html'
    return render(request, template_name)