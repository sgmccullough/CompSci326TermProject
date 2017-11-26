from django.shortcuts import render
from .models import Profile, Nugget, NuggetAttribute, Inventory, Shop, Item, Battle, Friend, InventoryItems, BattleInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, CreateNugget, CreateAttributes
from django.shortcuts import redirect

# Create your views here.

def index(request):
    """
    View function for login page.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #Profile.objects.filter(usr=username)
            #Nugget.objects.get(user=Profile.objects.get(usr=request.user)
            nugatt = NuggetAttribute.objects.create()
            inv = Inventory.objects.create(user=Profile.objects.get(usr=request.user))
            Nugget.objects.create(user=Profile.objects.get(usr=request.user), attributes=nugatt, inventory=inv)
            Battle.objects.create(user=Profile.objects.get(usr=request.user))
            Friend.objects.create(current_user=Profile.objects.get(usr=request.user))
            return redirect('create')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})

def home(request):
    """
    View function for the home.
    """

    #Profile Properties
    usr_id = Profile.objects.get(usr=request.user)
    coins = Profile.objects.filter(id=usr_id).values_list('coins', flat=True)
    user = Profile.objects.filter(id=usr_id).values_list('usr', flat=True)
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


    battle_history = Battle.objects.filter(user=usr_id).values_list('battles', flat=True)
    battles_list = [None]
    for i in battle_history:
        opponent_id = BattleInstance.objects.filter(id=i).values_list('opponent_id', flat=True)
        opponent_name = Nugget.objects.filter(user=opponent_id).values_list('name', flat=True)
        net_coins = BattleInstance.objects.filter(id=i).values_list('net_coins', flat=True)
        won_status = "Lost!"
        if net_coins[0] > 0:
            won_status = "Won!"
        if battles_list[0] == None:
            battles_list = [[opponent_name[0], str(net_coins[0]), won_status]]
        else:
            battles_list = battles_list + [[opponent_name[0], net_coins[0], won_status]]

    friends = Friend.objects.filter(current_user=usr_id).values_list('users', flat=True)
    friends_names = Nugget.objects.filter(user=friends[0]).values_list('name', flat=True)

    return render(
        request,
        'home.html',
        {'coins':coins[0], 'user':user[0], 'nugget':nugget[0], 'health':health[0], 'health_color':health_color, 'hunger':hunger[0], 'hunger_color':hunger_color,
        'happiness':happiness[0], 'happiness_color':happiness_color, 'battle_XP':battle_XP[0], 'battle_XP_color':battle_XP_color, "battles":battles_list,
         "friends":friends_names[0]},
    )

def nugget(request):
    """
    View function for nugget page.
    """
    usr_id = '78292571d46c4a0789d292d9e3d85ec8'

    #User Properties
    coins = Profile.objects.filter(id=usr_id).values_list('coins', flat=True)
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
        'happiness':happiness[0], 'happiness_color':happiness_color, 'luck':luck[0], 'luck_color':luck_color, 'items':item_names},
    )

def shop(request):
    """
    View function for shop page.
    """
    usr_id = '78292571d46c4a0789d292d9e3d85ec8'
    coins = Profile.objects.filter(id=usr_id).values_list('coins', flat=True)

    items = Item.objects.all()
    item_names = [None]
    for i in items:
        item_names = item_names + [getattr(i, 'name')]
    item_names = item_names[1:]

    inventory = Inventory.objects.filter(user=usr_id).values_list('id', flat=True)
    inv_items = Inventory.objects.filter(id=inventory).values_list('items', flat=True)
    quantities = InventoryItems.objects.filter(inventory=inventory).values_list('quantity', flat=True)

    inv_item_names = [None]
    counter = 0
    for i in inv_items:
        if inv_item_names[0] == None:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            inv_item_names = [[temp[0], quantities[counter]]]
        else:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            inv_item_names = inv_item_names + [[temp[0], quantities[counter]]]
        counter = counter + 1

    return render(
        request,
        'shop.html',
        {'coins':coins[0], 'items':item_names, 'inventory':inv_item_names}
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
    usr_id = '78292571d46c4a0789d292d9e3d85ec8'
    opp_id = '99daf529d7ed44f0934085983f768eb5'

    #Battle Properties
    # bat_id = Battle.objects.filter(user=usr_id).values_list('battles', flat=True)
    user = User.objects.filter(id=usr_id).values_list('usr', flat=True)
    nugget = Nugget.objects.filter(user=usr_id).values_list('name', flat=True)
    coins = Profile.objects.filter(id=usr_id).values_list('coins', flat=True)
    nug_xp = BattleInstance.objects.filter(id=usr_id).values_list('nug_xp', flat=True)
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


    battle_history = Battle.objects.filter(user=usr_id).values_list('battles', flat=True)
    # will need to make this a loop at some point in JS.
    opponent_id = BattleInstance.objects.filter(id=battle_history[0]).values_list('opponent_id', flat=True)
    opponent_name = Nugget.objects.filter(user=opponent_id[0]).values_list('name', flat=True)
    net_coins = BattleInstance.objects.filter(id=battle_history[0]).values_list('net_coins', flat=True)
    net_battle_XP = BattleInstance.objects.filter(id=battle_history[0]).values_list('nug_xp', flat=True)

    return render(
        request,
        'battle.html',
        {'coins':coins[0], 'nugget':nugget[0], 'user':user[0], 'health':health[0], 'health_color':health_color, 'hunger':hunger[0], 'hunger_color':hunger_color,
        'happiness':happiness[0], 'happiness_color':happiness_color, 'battle_XP':battle_XP[0], 'battle_XP_color':battle_XP_color, 'opponent_id':opponent_name[0],
        'net_coins':net_coins[0], 'net_battle_XP':net_battle_XP[0]},
    )

from django.shortcuts import render_to_response
import uuid

def create(request):
    """
    View function for create page.
    """
    rec = Nugget.objects.get(user=Profile.objects.get(usr=request.user))
    att = getattr(rec, 'attributes')
    if request.method == 'POST':
        n1 = CreateNugget(request.POST, instance=rec)
        n2 = CreateAttributes(request.POST, instance=att)
        if n1.is_valid() and n2.is_valid():
            n1.save()
            n2.save()
            return redirect('home')
        else:
            return render_to_response('errortemp.html', {'n2': n2})
    else:
        n1 = CreateNugget()
        n2 = CreateAttributes()

    # Attributes
    # shape = NuggetAttribute.objects.filter(id=att).values_list('nugget_status', flat=True)
    # size = NuggetAttribute.objects.filter(id=att).values_list('nug_size', flat=True)
    # color = NuggetAttribute.objects.filter(id=att).values_list('color', flat=True)
    # mouth_size = NuggetAttribute.objects.filter(id=att).values_list('mouth_size', flat=True)
    # mouth_shape = NuggetAttribute.objects.filter(id=att).values_list('mouth_status', flat=True)
    # eye_size = NuggetAttribute.objects.filter(id=att).values_list('eye_size', flat=True)
    # eye_shape = NuggetAttribute.objects.filter(id=att).values_list('eye_status', flat=True)
    shape = getattr(att, 'nugget_status')
    size = getattr(att, 'nug_size')
    color = getattr(att, 'color')
    mouth_size = getattr(att, 'mouth_size')
    mouth_shape = getattr(att, 'mouth_status')
    eye_size = getattr(att, 'eye_size')
    eye_shape = getattr(att, 'eye_status')

    return render(
        request,
        'create-a-nugget.html',
        {'shape':shape, 'size':size, 'color':color, 'mouth_size':mouth_size, 'mouth_shape':mouth_shape, 'eye_size':eye_size, 'eye_shape':eye_shape, 'n1': n1, 'n2': n2, },
    )
