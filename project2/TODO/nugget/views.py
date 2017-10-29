from django.shortcuts import render

# Create your views here.

from .models import User, Nugget, NuggetAttribute, Inventorie, Shop, Item, Battle, Nug_IDs, FriendsList

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
    return render(
        request,
        'battle.html',
    )

def create(request):  #Emily
    """
    View function for create page.
    """
    # Nugget attributes
    usr_id = 100
    test = NuggetAttribute.objects.all()
    nug_color = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('nug_color', flat=True)
    nug_size = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('nug_size', flat=True)
    mouth_size = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('mouth_size', flat=True)
    mouth_shape = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('mouth_status', flat=True)
    eye_size = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('eye_size', flat=True)
    eye_shape = NuggetAttribute.objects.filter(nug_id=usr_id).values_list('eye_status', flat=True)

    return render(
        request,
        'create-a-nugget.html',
        {'test':test},
        #{'nug_size':nug_size[0]},
        #, ,'nug_color':nug_color, 'mouth_size':mouth_size[0], 'eye_size':eye_size[0], 'eye_shape':eye_shape[0]
    )
