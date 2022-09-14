import os
import stripe
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic, Message
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
from django.http import HttpResponse

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')


    return render(request, 'base/login_register.html', {'form': form})

        
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'base/room.html', context)



def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')


    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
            )
    topics=Topic.objects.all()
    room_count=rooms.count()
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms':rooms,
               'topics': topics,
               'room_count': room_count,
               'room_messages': room_messages,
               }
    return render(request, 'base/home.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        print(request.POST)
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here.")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here.")

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here.")

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})


stripe.api_key = 'sk_test_51LhrHvFPj4UkaHNH6r2dgl899NPiyVOMoT18XLLQf5Riuxx52HZoaVdmCvyrqRBXQ1rPv7lRoJoGYJDZsz71LFsA009QVWfqSf'
stripe.Product.list(limit=3)
stripe.Price.list(product='prod_MQnrK9MxLd5Za7', active=True)
def checkoutRoom(self):
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],

    line_items=[{
        "price": "price_1LhwG8FPj4UkaHNH1j5e9LNo",
        
      
       'adjustable_quantity': {
        'enabled': True,
        'minimum': 1,
        'maximum': 10,
      },
      'quantity': 1,

    },
    {
        "price": "price_1LhzZiFPj4UkaHNHhwKw9rPf",
        'adjustable_quantity': {
            'enabled': True,
            'minimum': 1,
            'maximum': 10,
            },
        'quantity':1,
        }],

    discounts=[{
    'coupon': 'IB5EWVQj',
  }],


        mode='payment',          
        success_url='http://127.0.0.1:8000/successRoom',  
        cancel_url='https://example.com/cancel',          
        )

  subscription = stripe.Subscription.create(
  customer="cus_MQl9voKyImnFs3",
  items=[{'price': 'price_1LhtlcFPj4UkaHNH6zNgCjYh'}],
  coupon='CjfQGhuY',
)

  return redirect(session.url, code=303)

def productRoom(request):
    num_books = Room.objects.all().count()
    context = {
        'num_books': num_books
    }
        
    return render(request, 'base/productRoom.html', context=context)

def successRoom(request):
    return render(request, 'base/success.html')


