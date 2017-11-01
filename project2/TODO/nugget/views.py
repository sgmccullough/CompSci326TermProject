from django.shortcuts import render

# Create your views here.

from .models import User, Nugget, NuggetAttribute, Inventory, Shop, Item, Battle, Friend, InventoryItems, BattleInstance

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
    View function for the home.
    """
    usr_id = 'f029b8610d3e4748a4b5d0d56a76fac0'

    #User Properties
    coins = User.objects.filter(id=usr_id).values_list('coins', flat=True)
    user = User.objects.filter(id=usr_id).values_list('usr', flat=True)
    nugget = Nugget.objects.filter(user=usr_id).values_list('name', flat=True)
    nug_attributes = Nugget.objects.filter(user=usr_id).values_list('attributes', flat=True)

    health = NuggetAttribute.objects.filter(id=nug_attributes).values_list('health', flat=True)
    if health[0] > 50:
        health_color = "green"
    elif health[0] > 20:
        health_color = "orange"
    else:
        health_color = "red"

    hunger = NuggetAttribute.objects.filter(id=nug_attributes).values_list('hunger', flat=True)
    if hunger[0] > 50:
        hunger_color = "green"
    elif hunger[0] > 20:
        hunger_color = "orange"
    else:
        hunger_color = "red"

    happiness = NuggetAttribute.objects.filter(id=nug_attributes).values_list('happiness', flat=True)
    if happiness[0] > 50:
        happiness_color = "green"
    elif happiness[0] > 20:
        happiness_color = "orange"
    else:
        happiness_color = "red"

    battle_XP = NuggetAttribute.objects.filter(id=nug_attributes).values_list('battle_XP', flat=True)
    if battle_XP[0] > 50:
        battle_XP_color = "green"
    elif battle_XP[0] > 20:
        battle_XP_color = "orange"
    else:
        battle_XP_color = "red"

    return render(
        request,
        'home.html',
        {'coins':coins[0], 'user':user[0], 'nugget':nugget[0], 'health':health[0], 'health_color':health_color, 'hunger':hunger[0], 'hunger_color':hunger_color,
        'happiness':happiness[0], 'happiness_color':happiness_color, 'battle_XP':battle_XP[0], 'battle_XP_color':battle_XP_color},
    )

def nugget(request): #Pinak
    """
    View function for nugget page.
    """
    usr_id = 'f029b8610d3e4748a4b5d0d56a76fac0'

    #User Properties
    coins = User.objects.filter(id=usr_id).values_list('coins', flat=True)
    user = User.objects.filter(id=usr_id).values_list('usr', flat=True)
    nugget = Nugget.objects.filter(user=usr_id).values_list('name', flat=True)
    nug_attributes = Nugget.objects.filter(user=usr_id).values_list('attributes', flat=True)

    health = NuggetAttribute.objects.filter(id=nug_attributes).values_list('health', flat=True)
    if health[0] > 50:
        health_color = "green"
    elif health[0] > 20:
        health_color = "orange"
    else:
        health_color = "red"

    hunger = NuggetAttribute.objects.filter(id=nug_attributes).values_list('hunger', flat=True)
    if hunger[0] > 50:
        hunger_color = "green"
    elif hunger[0] > 20:
        hunger_color = "orange"
    else:
        hunger_color = "red"

    defense = NuggetAttribute.objects.filter(id=nug_attributes).values_list('defense', flat=True)
    if defense[0] > 50:
        defense_color = "green"
    elif defense[0] > 20:
        defense_color = "orange"
    else:
        defense_color = "red"

    battle_XP = NuggetAttribute.objects.filter(id=nug_attributes).values_list('battle_XP', flat=True)
    if battle_XP[0] > 50:
        battle_XP_color = "green"
    elif battle_XP[0] > 20:
        battle_XP_color = "orange"
    else:
        battle_XP_color = "red"

    fatigue = NuggetAttribute.objects.filter(id=nug_attributes).values_list('fatigue', flat=True)
    if fatigue[0] > 50:
        fatigue_color = "green"
    elif fatigue[0] > 20:
        fatigue_color = "orange"
    else:
        fatigue_color = "red"

    intelligence = NuggetAttribute.objects.filter(id=nug_attributes).values_list('intelligence', flat=True)
    if intelligence[0] > 50:
        intelligence_color = "green"
    elif intelligence[0] > 20:
        intelligence_color = "orange"
    else:
        intelligence_color = "red"

    happiness = NuggetAttribute.objects.filter(id=nug_attributes).values_list('happiness', flat=True)
    if happiness[0] > 50:
        happiness_color = "green"
    elif happiness[0] > 20:
        happiness_color = "orange"
    else:
        happiness_color = "red"

    luck = NuggetAttribute.objects.filter(id=nug_attributes).values_list('luck', flat=True)
    if luck[0] > 50:
        luck_color = "green"
    elif luck[0] > 20:
        luck_color = "orange"
    else:
        luck_color = "red"

    inventory = Inventory.objects.filter(user=usr_id).values_list('id', flat=True)
    items = Inventory.objects.filter(id=inventory).values_list('items', flat=True)
    quantities = InventoryItems.objects.filter(inventory=inventory).values_list('quantity', flat=True)

    item_names = [None]
    counter = 0
    for i in items:
        if item_names[0] == None:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            item_names = [[temp[0], quantities[counter]]]
        else:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            item_names = item_names + [[temp[0], quantities[counter]]]
        counter = counter + 1

    return render(
        request,
        'nugget.html',
        {'coins':coins[0], 'user':user[0], 'nugget':nugget[0], 'health':health[0], 'health_color':health_color, 'hunger':hunger[0],
        'hunger_color':hunger_color, 'defense':defense[0], 'defense_color':defense_color, 'battle_XP':battle_XP[0], 'battle_XP_color':battle_XP_color,
        'fatigue':fatigue[0], 'fatigue_color':fatigue_color, 'intelligence':intelligence[0], 'intelligence_color':intelligence_color,
        'happiness':happiness[0], 'happiness_color':happiness_color, 'luck':luck[0], 'luck_color':luck_color, 'items':item_names, 'item_1':item_names[0]},
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
    # Logistics
    usr_id = 'e954e5ed18ff44d9b98d7714a22f5145'
    nug_attributes = Nugget.objects.filter(user=usr_id).values_list('attributes', flat=True)

    # Attributes
    shape = NuggetAttribute.objects.filter(id=nug_attributes).values_list('nugget_status', flat=True)
    size = NuggetAttribute.objects.filter(id=nug_attributes).values_list('nug_size', flat=True)
    color = NuggetAttribute.objects.filter(id=nug_attributes).values_list('color', flat=True)
    mouth_size = NuggetAttribute.objects.filter(id=nug_attributes).values_list('mouth_size', flat=True)
    mouth_shape = NuggetAttribute.objects.filter(id=nug_attributes).values_list('mouth_status', flat=True)
    eye_size = NuggetAttribute.objects.filter(id=nug_attributes).values_list('eye_size', flat=True)
    eye_shape = NuggetAttribute.objects.filter(id=nug_attributes).values_list('eye_status', flat=True)

    return render(
        request,
        'create-a-nugget.html',
        {'shape':shape[0], 'size':size[0], 'color':color[0], 'mouth_size':mouth_size[0], 'mouth_shape':mouth_shape[0], 'eye_size':eye_size[0], 'eye_shape':eye_shape[0]},
    )
