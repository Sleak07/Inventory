from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the invent index.")


def about(request):
    return HttpResponse("Hello, world. You're at the about page.")


def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")