from django.shortcuts import redirect, render
from django.contrib import messages

from page.forms import RegisterForm

# Create your views here.
def page_index(request):
    return render(request, "index.html")


def page_tutor(request):
    return render(request, "tutor.html")


def page_lesson(request):
    return render(request, "lesson.html")


def page_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # save form on database
            form.save()

            # add success message
            messages.success(request, 'Success!')
        
            return redirect("/auth")
        
        else:
            # Adicionar error message - danger
            messages.error(request, 'Please correct errors in the form before submitting.', extra_tags='alert-danger')
   
        
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {'form':form})


def page_auth(request):
    return render(request, "auth.html")

def page_contact(request):
    return render(request, "contact.html")

def page_about(request):
    return render(request, "about.html")
