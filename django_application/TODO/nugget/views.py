from .models import Profile, Nugget, NuggetAttribute, Inventory, Shop, Item, Battle, Friend, InventoryItems, BattleInstance, News
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, CreateNugget, CreateAttributes, InventoryForm, NewBattle
from django.shortcuts import redirect, render_to_response, render
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
import uuid
from django.template import Context, Template

# Create your views here.

def index(request):
    """
    View function for login page.
    """
    if request.user.is_authenticated:
        return redirect('home')
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

@login_required(login_url='/nugget/')
def home(request):
    """
    View function for the home.
    """

    #Profile Properties
    usr_id = Profile.objects.get(usr=request.user)
    user = getattr(usr_id, 'usr')
    nugget = Nugget.objects.get(user=usr_id)
    coins = getattr(usr_id, 'coins')
    nug_attributes = getattr(nugget, 'attributes')

    if getattr(nugget, 'name') is "":
        return redirect('create')

    #Nugget attributes
    shape = getattr(nug_attributes, 'nugget_status')
    size = getattr(nug_attributes, 'nug_size')
    color = getattr(nug_attributes, 'color')
    mouth_size = getattr(nug_attributes, 'mouth_size')
    mouth_shape = getattr(nug_attributes, 'mouth_status')
    eye_size = getattr(nug_attributes, 'eye_size')
    eye_shape = getattr(nug_attributes, 'eye_status')

    health = getattr(nug_attributes, 'health')
    hunger = getattr(nug_attributes, 'hunger')
    happiness = getattr(nug_attributes, 'happiness')
    battle_XP = getattr(nug_attributes, 'battle_XP')

    if health > 50:
        health_color = "green"
    elif health > 20:
        health_color = "orange"
    else:
        health_color = "red"

    if hunger > 50:
        hunger_color = "green"
    elif hunger > 20:
        hunger_color = "orange"
    else:
        hunger_color = "red"

    if happiness > 50:
        happiness_color = "green"
    elif happiness > 20:
        happiness_color = "orange"
    else:
        happiness_color = "red"

    if battle_XP > 50:
        battle_XP_color = "green"
    elif battle_XP > 20:
        battle_XP_color = "orange"
    else:
        battle_XP_color = "red"


    battle_set = Battle.objects.get(user=Profile.objects.get(usr=request.user))
    battle_history = getattr(battle_set, 'battles')
    battles_list = [None]
    maxVal = 0;
    for i in battle_history.iterator():
        if maxVal > 2:
            break
        opponent_id = getattr(i, 'opponent_id')
        opponent_name = getattr(Nugget.objects.get(user=opponent_id), 'name')
        net_coins = getattr(i, 'net_coins')
        won_status = "Lost!"
        if net_coins > 0:
            won_status = "Won!"
        if battles_list[0] == None:
            battles_list = [[opponent_name, str(net_coins), won_status]]
        else:
            battles_list = battles_list + [[opponent_name, net_coins, won_status]]
        maxVal+=1

    if battles_list[0] == None:
        battles_list = ["No recent battles.", "-", "-"]

    friends = Friend.objects.get(current_user=usr_id)
    friends_names = getattr(friends, 'users')
    list_friends = []

    for i in friends_names.iterator():
        nug = Nugget.objects.get(user=i)
        list_friends.append(getattr(nug, 'name'))

    news = News.objects.all().values_list('text', flat=True)
    newsList = []

    for i in news.iterator():
        newsList.append(i)

    return render(
        request,
        'home.html',
        {'coins':coins, 'user':user, 'nugget':nugget, 'color':color, 'mouth':mouth_shape, 'health':health, 'health_color':health_color, 'hunger':hunger, 'hunger_color':hunger_color,
        'happiness':happiness, 'happiness_color':happiness_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color, "battles":battles_list,
         'friends':list_friends, 'news': newsList, },
    )

@login_required(login_url='/nugget/')
def nugget(request):
    """
    View function for nugget page.
    """
    #User Properties
    usr_id = Profile.objects.get(usr=request.user)
    user = getattr(usr_id, 'usr')
    nugget = Nugget.objects.get(user=usr_id)
    coins = getattr(usr_id, 'coins')
    nug_attributes = getattr(nugget, 'attributes')

    if getattr(nugget, 'name') is "":
        return redirect('create')

    #Nugget attributes
    shape = getattr(nug_attributes, 'nugget_status')
    size = getattr(nug_attributes, 'nug_size')
    color = getattr(nug_attributes, 'color')
    mouth_size = getattr(nug_attributes, 'mouth_size')
    mouth = getattr(nug_attributes, 'mouth_status')
    eye_size = getattr(nug_attributes, 'eye_size')
    eye_shape = getattr(nug_attributes, 'eye_status')

    health = getattr(nug_attributes, 'health')
    hunger = getattr(nug_attributes, 'hunger')
    happiness = getattr(nug_attributes, 'happiness')
    battle_XP = getattr(nug_attributes, 'battle_XP')
    fatigue = getattr(nug_attributes, 'fatigue')
    defense = getattr(nug_attributes, 'defense')
    intelligence = getattr(nug_attributes, 'intelligence')
    luck = getattr(nug_attributes, 'luck')

    #Nugget attributes views
    #health = NuggetAttribute.objects.filter(id=nug_attributes).values_list('health', flat=True)
    if health > 50:
        health_color = "green"
    elif health > 20:
        health_color = "orange"
    else:
        health_color = "red"

    #hunger = NuggetAttribute.objects.filter(id=nug_attributes).values_list('hunger', flat=True)
    if hunger > 50:
        hunger_color = "green"
    elif hunger > 20:
        hunger_color = "orange"
    else:
        hunger_color = "red"

    #happiness = NuggetAttribute.objects.filter(id=nug_attributes).values_list('happiness', flat=True)
    if happiness > 50:
        happiness_color = "green"
    elif happiness > 20:
        happiness_color = "orange"
    else:
        happiness_color = "red"

    #battle_XP = NuggetAttribute.objects.filter(id=nug_attributes).values_list('battle_XP', flat=True)
    if battle_XP > 50:
        battle_XP_color = "green"
    elif battle_XP > 20:
        battle_XP_color = "orange"
    else:
        battle_XP_color = "red"

    #defense = NuggetAttribute.objects.filter(id=nug_attributes).values_list('defense', flat=True)
    if defense > 50:
        defense_color = "green"
    elif defense > 20:
        defense_color = "orange"
    else:
        defense_color = "red"

    #fatigue = NuggetAttribute.objects.filter(id=nug_attributes).values_list('fatigue', flat=True)
    if fatigue > 50:
        fatigue_color = "green"
    elif fatigue > 20:
        fatigue_color = "orange"
    else:
        fatigue_color = "red"

    #intelligence = NuggetAttribute.objects.filter(id=nug_attributes).values_list('intelligence', flat=True)
    if intelligence > 50:
        intelligence_color = "green"
    elif intelligence > 20:
        intelligence_color = "orange"
    else:
        intelligence_color = "red"

    #luck = NuggetAttribute.objects.filter(id=nug_attributes).values_list('luck', flat=True)
    if luck > 50:
        luck_color = "green"
    elif luck > 20:
        luck_color = "orange"
    else:
        luck_color = "red"

    inventory = Inventory.objects.filter(user=usr_id).values_list('id', flat=True)
    items = Inventory.objects.filter(id=inventory).values_list('items', flat=True)
    quantities = InventoryItems.objects.filter(inventory=inventory).values_list('quantity', flat=True)

    item_names = [None]
    counter = 0
    counter2 = 0
    for i in items:
        if item_names[0] == None:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            if len(temp) is not 0:
                item_names = [[temp[0], quantities[counter]]]
        else:
            temp = Item.objects.filter(id=i).values_list('name', flat=True)
            item_names = item_names + [[temp[0], quantities[counter]]]
        counter = counter + 1
        counter2 = counter2 + 1

    #Inventory Form Set
    InventoryFormSet = formset_factory(InventoryForm, extra=counter2)
    queryset = Inventory.objects.filter(id=inventory).values_list('items', flat=True)
    if request.method == 'POST':
        FormSet = InventoryFormSet(request.POST)
        for form in FormSet.forms:
            if form.is_valid():
                form.save()
                submission = form.cleaned_data.get('ItemOptions')
                #if submission is "feed":

        return redirect('nugget')
    else:
        FormSet = InventoryFormSet()

    return render(
        request,
        'nugget.html',
        {'coins':coins, 'user':user, 'nugget':nugget, 'health':health, 'health_color':health_color, 'hunger':hunger, 'mouth': mouth, 'color':color,
        'hunger_color':hunger_color, 'defense':defense, 'defense_color':defense_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color,
        'fatigue':fatigue, 'fatigue_color':fatigue_color, 'intelligence':intelligence, 'intelligence_color':intelligence_color,
        'happiness':happiness, 'happiness_color':happiness_color, 'luck':luck, 'luck_color':luck_color, 'items':item_names, 'form': FormSet},
    )

@login_required(login_url='/nugget/')
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

@login_required(login_url='/nugget/')
def chat(request):
    """
    View function for chat page.
    """
    return render(
        request,
        'chat.html',
    )

@login_required(login_url='/nugget/')
def battle(request):
    """
    View function for battle page.
    """

    usr_id = Profile.objects.get(usr=request.user)

    #Battle Properties
    # bat_id = Battle.objects.filter(user=usr_id).values_list('battles', flat=True)
    nugget = Nugget.objects.get(user=usr_id)
    coins = getattr(usr_id, 'coins')

    nug_attributes = getattr(nugget, 'attributes')

    color = getattr(nug_attributes, 'color')
    mouth = getattr(nug_attributes, 'mouth_status')

    health = getattr(nug_attributes, 'health')
    hunger = getattr(nug_attributes, 'hunger')
    happiness = getattr(nug_attributes, 'happiness')
    battle_XP = getattr(nug_attributes, 'battle_XP')
    #net_coins = getattr(battle, 'coins')

    if health > 50:
        health_color = "green"
    elif health > 20:
        health_color = "orange"
    else:
        health_color = "red"

    if hunger > 50:
        hunger_color = "green"
    elif hunger > 20:
        hunger_color = "orange"
    else:
        hunger_color = "red"

    if happiness > 50:
        happiness_color = "green"
    elif happiness > 20:
        happiness_color = "orange"
    else:
        happiness_color = "red"

    if battle_XP > 50:
        battle_XP_color = "green"
    elif battle_XP > 20:
        battle_XP_color = "orange"
    else:
        battle_XP_color = "red"


    battle_set = Battle.objects.get(user=Profile.objects.get(usr=request.user))
    battle_history = getattr(battle_set, 'battles')
    #battle_history = Battle.objects.filter(user=usr_id).values_list('battles', flat=True)
    battles_list = [None]
    #return render_to_response('errortemp_2.html', {'val': battle_history})
    maxVal = 0;
    for i in battle_history.iterator():
        if maxVal > 2:
            break
        opponent_id = getattr(i, 'opponent_id')
        opponent_name = getattr(Nugget.objects.get(user=opponent_id), 'name')
        net_coins = getattr(i, 'net_coins')
        # opponent_id = BattleInstance.objects.filter(id=i).values_list('opponent_id', flat=True)
        # opponent_name = Nugget.objects.filter(user=opponent_id).values_list('name', flat=True)
        # net_coins = BattleInstance.objects.filter(id=i).values_list('net_coins', flat=True)
        won_status = "Lost!"
        if net_coins > 0:
            won_status = "Won!"
        if battles_list[0] == None:
            battles_list = [[opponent_name, str(net_coins), won_status]]
        else:
            battles_list = battles_list + [[opponent_name, net_coins, won_status]]
        maxVal+=1

    if battles_list[0] == None:
        battles_list = ["No recent battles.", "-", "-"]

    friends = Friend.objects.get(current_user=usr_id)
    friends_names = getattr(friends, 'users')
    list_friends = []

    for i in friends_names.iterator():
        nug = Nugget.objects.get(user=i)
        list_friends.append(getattr(nug, 'name'))

    #return render_to_response('errortemp_2.html', {'val': request.method,})
    thisUser = request.user
    if hasattr(thisUser, '_wrapped') and hasattr(thisUser, '_setup'):
        if thisUser._wrapped.__class__ == object:
            thisUser._setup()
        thisUser = thisUser._wrapped

    if request.method == 'POST':
        newBattle = NewBattle(request.POST, user=thisUser)
        if newBattle.is_valid():
            newBattle.save()
    else:
        newBattle =  NewBattle(user=thisUser)

    return render(
        request,
        'battle.html',
        {'coins':coins, 'nugget':nugget, 'health':health, 'health_color':health_color, 'hunger':hunger, 'hunger_color':hunger_color,
        'happiness':happiness, 'happiness_color':happiness_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color, 'opponents':list_friends,
        'color':color, 'mouth':mouth, 'battles':battles_list, 'newBattle': newBattle,},
    )

@login_required(login_url='/nugget/')
def create(request):
    """
    View function for create page.
    """
    rec = Nugget.objects.get(user=Profile.objects.get(usr=request.user))
    att = getattr(rec, 'attributes')

    # Remove this when editing the create page.
    if getattr(rec, 'name') is not "":
        return redirect('home')

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

    return render(
        request,
        'create-a-nugget.html',
        {'n1': n1, 'n2': n2, },
    )
