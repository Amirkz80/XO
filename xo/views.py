from django.shortcuts import render

def index(request):
  """Renders the main page"""
  return render(request, 'xo/xo.html')