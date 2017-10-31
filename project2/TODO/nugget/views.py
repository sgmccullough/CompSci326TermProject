from django.shortcuts import render

# Create your views here.

from .models import User, Nugget, NuggetAttribute, Inventory, Shop, Item, Battle, Nug_IDs, FriendsList

def index(request): #Scott
    """
    View function for login page.
    """
    return render(
        request,
        'index.html',
    )

def home(request):
    """
    View function for the template/navigation bar.
    """
    usr_id = 100
    coins = User.objects.filter(nug_id=usr_id).values_list('coins', flat=True)
    user = User.objects.filter(nug_id=usr_id).values_list('usr', flat=True)
    #nug_name = Nugget.objects.filter(nug_id=usr_id).values_list('name', flat=True)
    #user=User.objects.get(nug_id__User=100)
    return render(
        request,
        'home.html',
        {'coins':coins[0], 'user':user[0]},
    )

def nugget(request): #Pinak
    """
    View function for nugget page.
    """
    coins=User.objects.all().count()
    return render(
        request,
        'nugget.html',
        context={'coins':coins},
    )

def shop(request): #Arwa
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

def battle(request): #Malachai
    """
    View function for battle page.
    """

    usr_id = 100
    opp_id = 101
    bat_id = Battle.objects.filter(nug_id__pk=1).values_list('battle_id', flat=True)
    nug_id = Battle.objects.filter(pk=100).values_list('nug_id', flat=True)
    net_coin = Battle.objects.filter(nug_id__pk=1).values_list('net_coins', flat=True)
    opponent_id = User.objects.filter(nug_id=opp_id).values_list('nug_id', flat=True)
    nug_xp = Battle.objects.filter(nug_id__pk=1).values_list('nug_xp', flat=True)
    return render(
        request,
        'battle.html',
        {'bat_id':bat_id[0], 'nug_id':nug_id,'net_coin':net_coin[0],'opponent_id':opponent_id[0],
        'nug_xp':nug_xp[0]},
    )

def create(request):  #Emily
    """
    View function for create page.
    """
    # Nugget attributes
    usr_id = 100
    nug_size = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('nug_size', flat=True)
    nug_color = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('nug_color', flat=True)
    mouth_size = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('mouth_size', flat=True)
    mouth_shape = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('mouth_status', flat=True)
    eye_size = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('eye_size', flat=True)
    eye_shape = NuggetAttribute.objects.filter(nug_id__pk=1).values_list('eye_status', flat=True)

    return render(
        request,
        'create-a-nugget.html',
        {'nug_size':nug_size[0], 'nug_color':nug_color[0], 'mouth_size':mouth_size[0], 'eye_size':eye_size[0], 'eye_shape':eye_shape[0]},
    )
