from django.shortcuts import render, redirect
from .form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user =form.save()
      login(request, user)
      messages.success(request, 'Registration successful')
      return redirect('login')
    messages.error(request,'Unsuccessful registration, Invalid crediential')
  form = NewUserForm()
  return render(request,'users/register.html',context ={"register_form":form})

def loginUser(request):
  if request.method == "POST":
    form =AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged as {username}.")
        return redirect('home')
      else:
        messages.error(request, "Invalid username or password")
    else:
      messages.error(request, "Invalid username or password")
  form = AuthenticationForm()
  return render(request, "users/login.html",context={"login_form":form} )

def logoutUser(request):
  logout(request)
  messages.info(request, "you have been logged out")
  return redirect('home')
