from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from recursos.models import Recurso


def home(request):
    recursos = Recurso.objects.all()[:8]  # mostrar solo 8 recursos en portada
    context = {
        'recursos': recursos
    }
    return render(request, 'core/home.html', context)

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect("home")

#     return render(request, "core/login.html")

# def dashboard(request):
#     return render(request, 'core/dashboard.html')

# def register(request):
#     if request.method == "POST":
#         User.objects.create_user(
#             username=request.POST["username"],
#             email=request.POST["email"],
#             password=request.POST["password1"],
#             first_name=request.POST["first_name"],
#             last_name=request.POST["last_name"],
#         )
#         return redirect("login")

#     return render(request, "core/register.html")

# def register_view(request):
#     return render(request, "core/register.html")


