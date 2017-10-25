from django.shortcuts import render

# Create your views here.

from .models import User, Nugget, NuggetAttribute, Inventorie, Shop, Item, Battle, Nug_IDs, FriendsList

def index(request):
    """
    View function for login page.
    """
    return render(
        request,
        'index.html',
    )

def home(request):
    """
    View function for home page.
    """
    return render(
        request,
        'home.html',
    )

def nugget(request):
    """
    View function for nugget page.
    """
    return render(
        request,
        'nugget.html',
    )

def shop(request):
    """
    View function for shop page.
    """
    return render(
        request,
        'shop.html',
    )

def chat(request):
    """
    View function for chat page.
    """
    return render(
        request,
        'chat.html',
    )

def battle(request):
    """
    View function for battle page.
    """
    return render(
        request,
        'battle.html',
    )

def create(request):
    """
    View function for create page.
    """
    return render(
        request,
        'create-a-nugget.html',
    )
