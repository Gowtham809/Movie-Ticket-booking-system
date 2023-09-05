from django.shortcuts import render

# Create your views here.
# views.py
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import *
#@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

#@unauthenticated_user
def user_signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            my_group = Group.objects.filter(name='customer').count()
            print(my_group)

            username = form.cleaned_data.get('username')

            if my_group == 0:
                my_group = Group.objects.create(name='customer')
                Group.objects.create(name='admin')
            else:
                my_group = Group.objects.get(name='customer')

            user = form.save()
            user = User.objects.get(username=username)
            user.groups.add(my_group) #Add this user to customers group
            messages.success(request, 'Account is created successfully for '+ username)
            return redirect('login')
 
    context = {'form' : form}

    return render(request, 'register.html', context)

@login_required(login_url='login')      
@admin_only
def home(request):
    movie_tickets = MovieTickets.objects.all()
    return render(request, 'movie_tickets_list.html', {'movie_tickets': movie_tickets})

def logoutUser(request):
	logout(request)
	return redirect('login')


from django.shortcuts import render
from .models import MovieTickets
@login_required(login_url='login')      
@admin_only
def movie_tickets_list(request):
    movie_tickets =MovieTickets.objects.order_by('release_date')

    #print(movie_tickets)
    return render(request, 'movie_tickets_list.html', {'movie_tickets': movie_tickets})


def movie_page(request):
    movie_tickets =MovieTickets.objects.order_by('release_date')
    return render(request, 'home_1.html', {'movie_tickets': movie_tickets})

