from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

from page.forms import RegisterForm, AuthForm
from user.models import User 

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
    if request.method == 'POST':
        form = AuthForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user and check_password(password, user.password):
                # Usuário autenticado com sucesso
                messages.success(request, 'Login bem-sucedido. Bem-vindo de volta!')
                return redirect('index')  # Substitua 'página_inicial' pela URL desejada
            else:
                # Autenticação falhou
                messages.error(request, 'Erro ao fazer login. Verifique suas credenciais.')

            
           
    else:
        form = AuthForm()

    return render(request, 'auth.html', {'form': form})
   

def page_contact(request):
    return render(request, "contact.html")

def page_about(request):
    return render(request, "about.html")
