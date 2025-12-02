from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import PerfilUsuario, Rol
from .forms import RegistroForm


def register_view(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():
            identification = form.cleaned_data.get("identification")
            cellphonenumber = form.cleaned_data.get("cellphonenumber")

            print("cleaned_data:", form.cleaned_data)


            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password1"]
            )

            rol_cliente, _ = Rol.objects.get_or_create(nombre="Cliente")

            PerfilUsuario.objects.create(
                user=user,
                identification=identification,
                cellphonenumber=cellphonenumber,
                rol=rol_cliente
            )

            messages.success(request, "Cuenta creada correctamente.")
            return redirect("login")

    else:
        form = RegistroForm()

    return render(request, "usuarios/register.html", {"form": form})


# def register_view(request):
#     if request.method == "POST":
#         form = RegistroForm(request.POST)

#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data["username"],
#                 email=form.cleaned_data["email"],
#                 first_name=form.cleaned_data["first_name"],
#                 last_name=form.cleaned_data["last_name"],
#                 password=form.cleaned_data["password1"]
#             )

#             rol_cliente, _ = Rol.objects.get_or_create(nombre="Cliente")

#             PerfilUsuario.objects.create(
#                 user=user,
#                 identification=form.cleaned_data["identification"],
#                 cellphonenumber=form.cleaned_data["cellphonenumber"],
#                 rol=rol_cliente
#             )

#             messages.success(request, "Cuenta creada correctamente.")
#             return redirect("login")

#     else:
#         form = RegistroForm()

#     return render(request, "usuarios/register.html", {"form": form})




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Tu cuenta está inactiva.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "usuarios/login.html")


