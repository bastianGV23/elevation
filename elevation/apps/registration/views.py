from .forms import userForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash,login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
# Create your views here.

def registro(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')#toma el elemento password que se instancia en el template
            user = authenticate(email=user.email, password=raw_password)#autentica con el user mail que se agrega en el template y el password que se saca del template
            login(request, user)#se logea con el usuario
            return redirect('menu')
    else:
        form = userForm()
    return render(request, 'Registration/registro.html',{'form':form})
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'La contraseña ha sido cambiada')
            return redirect('contraseña')
        else:
            messages.error(request, 'Favor de colocar contraseña correcta')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/cambiar_pass.html', {
        'form': form
    })   


