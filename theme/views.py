from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def blog_redirect(request):
  return redirect("/", permanent=True)
