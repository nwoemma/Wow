from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'pages/index.html')
def about(request):
  return render(request, 'pages/about.html')
def contact(request):
  return render(request, 'pages/contact.html')
def shop(request):
  return render(request, "pages/shop.html")