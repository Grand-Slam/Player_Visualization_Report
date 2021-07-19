from django.shortcuts import render, get_object_or_404, redirect #get_object_or_404 추가, redirect
# Create your views here.

def home(request):
    return render(request, 'index.html')