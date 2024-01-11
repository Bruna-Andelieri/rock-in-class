from django.shortcuts import render

from page.forms import RegisterForm

# Create your views here.
def page_index(request):
    return render(request, "index.html")


def page_tutor(request):
    return render(request, "tutor.html")


def page_lesson(request):
    return render(request, "lesson.html")


def page_register(request):
    form = RegisterForm()
    return render(request, "register.html", {'form':form})


def page_auth(request):
    return render(request, "auth.html")

def page_contact(request):
    return render(request, "contact.html")

def page_about(request):
    return render(request, "about.html")
