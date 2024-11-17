from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import auther, qu
from .models import quote
from logging import error
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import random

class api(APIView):
    def get(self, request):
        queryset = quote.objects.all().order_by('-id').first()
        serializer = qu(queryset)
        return Response(
            {
                "status" : "success",
                "quote" : serializer.data.get('quote'),
                "author" : serializer.data.get('author')
            }
        )


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'app/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'app/login.html', context)
@login_required(login_url='login')
def home(requset):
    queryset = quote.objects.all().order_by('-id').first()
    latest_id = quote.objects.latest('id').id
    query = quote.objects.exclude(id=latest_id).order_by('-id')
    return render(requset,'app/next.html',{'queryset':queryset,'query':query})
@login_required(login_url='login')
def dele(request):
    user = request.user
    s = get_object_or_404(User, user=user)
    s.delete()
    return redirect('login')
def log(request):
    logout(request)
    return redirect('reg')
@login_required(login_url='login')
def apiinfo(request):
    return render(request,'app/api.html')