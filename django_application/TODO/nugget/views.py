from .models import Profile, Nugget, NuggetAttribute, Inventory, Shop, Item, Battle, Friend, InventoryItems, BattleInstance, News
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, CreateNugget, CreateAttributes, InventoryForm, NewBattle, BattleReset, BattleResponse, InventoryFormShop, ShopPurchase
from django.shortcuts import redirect, render_to_response, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.forms import formset_factory
import uuid
from django.template import Context, Template, RequestContext

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
            nugatt = NuggetAttribute.objects.create()
            inv = Inventory.objects.create(user=Profile.objects.get(usr=request.user))
            Nugget.objects.create(user=Profile.objects.get(usr=request.user), attributes=nugatt, inventory=inv)
            Battle.objects.create(user=Profile.objects.get(usr=request.user))
            Friend.objects.create(current_user=Profile.objects.get(usr=request.user))
            InventoryItems.objects.create(inventory=inv,item=Item.objects.get(name='Apple'),quantity=10)
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
    user = usr_id.usr
    nugget = Nugget.objects.get(user=usr_id)
    coins = usr_id.coins
    nug_attributes = nugget.attributes

    if nugget.name is "":
        return redirect('create')

    #Nugget attributes
    shape = nug_attributes.nugget_status

    if shape == 'c':
        size_w = 200
        size_h = 200
    else:
        size_w = 160
        size_h = 200

    color = nug_attributes.color
    mouth_shape = nug_attributes.mouth_status
    eye_size_h = nug_attributes.eye_size
    eye_size_w = eye_size_h*0.75

    health = nug_attributes.health
    hunger = nug_attributes.hunger
    happiness = nug_attributes.happiness
    battle_XP = nug_attributes.battle_XP

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


    battle_set = Battle.objects.get(user=usr_id)
    battle_history = battle_set.battles
    battles_list = [None]
    maxVal = 0;
    for i in battle_history.iterator():
        if maxVal > 2:
            break
        opponent_id1 = i.opp_a
        opponent_id2 = i.opp_b
        if opponent_id1 == usr_id:
            opponent_id = opponent_id1
        else:
            opponent_id = opponent_id2
        opponent_name = Nugget.objects.get(user=opponent_id).name
        net_coins = i.net_coins
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
    friends_names = friends.users
    list_friends = []

    for i in friends_names.iterator():
        nug = Nugget.objects.get(user=i)
        list_friends.append(nug.name)
    if list_friends == []:
        list_friends = "None"

    news = News.objects.all().values_list('text', flat=True)
    newsList = []

    for i in news.iterator():
        newsList.append(i)
    if newsList == []:
        newsList = "No News Currently. Check Back Later!"

    return render(
        request,
        'home.html',
        {'coins':coins, 'user':user, 'nugget':nugget, 'color':color, 'mouth':mouth_shape, 'health':health, 'eye_size_h': eye_size_h, 'eye_size_w': eye_size_w, 'health_color':health_color, 'hunger':hunger,
        'size_w': size_w, 'size_h': size_h, 'hunger_color':hunger_color, 'happiness':happiness, 'happiness_color':happiness_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color, "battles":battles_list,
         'friends':list_friends, 'news': newsList, },
    )

@login_required(login_url='/nugget/')
def nugget(request):
    """
    View function for nugget page.
    """
    #User Properties
    usr_id = Profile.objects.get(usr=request.user)
    user = usr_id.usr
    nugget = Nugget.objects.get(user=usr_id)
    coins = usr_id.coins
    nug_attributes = nugget.attributes

    if nugget.name is "":
        return redirect('create')

    #Nugget attributes
    shape = nug_attributes.nugget_status

    if shape == 'c':
        size_w = 200
        size_h = 200
    else:
        size_w = 160
        size_h = 200
    eye_size_h = nug_attributes.eye_size
    eye_size_w = eye_size_h*0.75

    color = nug_attributes.color
    mouth = nug_attributes.mouth_status
    eye_size = nug_attributes.eye_size

    health = nug_attributes.health
    hunger = nug_attributes.hunger
    happiness = nug_attributes.happiness
    battle_XP = nug_attributes.battle_XP
    fatigue = nug_attributes.fatigue
    defense = nug_attributes.defense
    intelligence = nug_attributes.intelligence
    luck = nug_attributes.luck

    #Nugget attributes views
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

    if defense > 50:
        defense_color = "green"
    elif defense > 20:
        defense_color = "orange"
    else:
        defense_color = "red"

    if fatigue > 50:
        fatigue_color = "green"
    elif fatigue > 20:
        fatigue_color = "orange"
    else:
        fatigue_color = "red"

    if intelligence > 50:
        intelligence_color = "green"
    elif intelligence > 20:
        intelligence_color = "orange"
    else:
        intelligence_color = "red"

    if luck > 50:
        luck_color = "green"
    elif luck > 20:
        luck_color = "orange"
    else:
        luck_color = "red"

   # Update the GUI for a user's inventory
    inventory = Inventory.objects.get(user=usr_id)
    items = InventoryItems.objects.filter(inventory=inventory)
    item_names = []
    for i in items:
        currItem = Item.objects.get(name=i.item.name)
        attributeToChange = currItem.item_features
        if attributeToChange == 'he':
            attributeToChange = "Health"
        elif attributeToChange == 'hun':
            attributeToChange = "Hunger"
        elif attributeToChange == 'def':
            attributeToChange = "Defense"
        elif attributeToChange == 'f':
            attributeToChange = "Fatigue"
        elif attributeToChange == 'i':
            attributeToChange = "Intelligence"
        elif attributeToChange == 'happ':
            attributeToChange = "Happiness"
        elif attributeToChange == 'l':
            attributeToChange = "Luck"
        else:
            attributeToChange = "Unknown."
        item_names.append([currItem.name, i.quantity, attributeToChange, currItem.effect])
    if item_names == []:
        item_names = "None"

    # Form Logic
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        itemToUpdate = request.POST.get('item_id', None)
        #return render_to_response('errortemp_2.html', {'val': temp})
        if form.is_valid():
            form.save()
            quantityToUpdate = form.cleaned_data.get('ItemQuantity')
            # Removes Items From Inventory
            for i in items:
                currentItem = Item.objects.get(name=i.item.name)
                if currentItem.name == itemToUpdate:
                    objectToUpdate = InventoryItems.objects.get(inventory=inventory, item=currentItem)
                    #objectToUpdate.update(quantity=F('quantity')+1)
                    if objectToUpdate.quantity - quantityToUpdate >= 0:
                        objectToUpdate.quantity -= quantityToUpdate
                        objectToUpdate.save()
                    else:
                        return redirect('nugget')
                    #return render_to_response('errortemp_2.html', {'val': objectToUpdate.quantity})
            if objectToUpdate.quantity <= 0:
                objectToUpdate.delete()


            # Updates coins/attributes of the item that we acted upon
            whatToDoWithItem = form.cleaned_data.get('ItemOptions')
            if whatToDoWithItem == 'feed':
                itemToWorkWith = Item.objects.get(name=itemToUpdate)
                attributeOfItem = itemToWorkWith.item_features
                amountToAddToAttribute = itemToWorkWith.effect * quantityToUpdate
                usersAttributeToUpdate = nug_attributes
                if attributeOfItem == 'he':
                    if usersAttributeToUpdate.health + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.health = 100
                    else:
                        usersAttributeToUpdate.health += amountToAddToAttribute
                elif attributeOfItem == 'hun':
                    if usersAttributeToUpdate.hunger + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.hunger = 100
                    else:
                        usersAttributeToUpdate.hunger += amountToAddToAttribute
                elif attributeOfItem == 'def':
                    if usersAttributeToUpdate.defense + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.defense = 100
                    else:
                        usersAttributeToUpdate.defense += amountToAddToAttribute
                elif attributeOfItem == 'f':
                    if usersAttributeToUpdate.fatigue + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.fatigue = 100
                    else:
                        usersAttributeToUpdate.fatigue += amountToAddToAttribute
                elif attributeOfItem == 'i':
                    if usersAttributeToUpdate.intelligence + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.intelligence = 100
                    else:
                        usersAttributeToUpdate.intelligence += amountToAddToAttribute
                elif attributeOfItem == 'happ':
                    if usersAttributeToUpdate.happiness + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.happiness = 100
                    else:
                        usersAttributeToUpdate.happiness += amountToAddToAttribute
                elif attributeOfItem == 'l':
                    if usersAttributeToUpdate.luck + amountToAddToAttribute > 100:
                        usersAttributeToUpdate.luck = 100
                    else:
                        usersAttributeToUpdate.luck += amountToAddToAttribute
                usersAttributeToUpdate.save()

                #return render_to_response('errortemp_2.html', {'val': attributeObjectToUpdate})
            if whatToDoWithItem == 'sell':
                priceOfTheItem = Item.objects.get(name=itemToUpdate).price
                amountToAddToCoins = priceOfTheItem * quantityToUpdate
                usr_id.coins += amountToAddToCoins
                usr_id.save()
            # We dont really care about discard, it just removes the item anyways.
            #if whatToDoWithItem == 'discard':
            #    return render_to_response('errortemp_2.html', {'val': whatToDoWithItem})
        return redirect('nugget')
    else:
        form = InventoryForm()

    #return render_to_response('errortemp_2.html', {'val': form})

    return render(
        request,
        'nugget.html',
        {'coins':coins, 'user':user, 'nugget':nugget, 'health':health, 'health_color':health_color, 'hunger':hunger, 'mouth': mouth, 'color':color,
        'size_w':size_w, 'size_h':size_h, 'eye_size_w':eye_size_w, 'eye_size_h':eye_size_h,
        'hunger_color':hunger_color, 'defense':defense, 'defense_color':defense_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color,
        'fatigue':fatigue, 'fatigue_color':fatigue_color, 'intelligence':intelligence, 'intelligence_color':intelligence_color,
        'happiness':happiness, 'happiness_color':happiness_color, 'luck':luck, 'luck_color':luck_color, 'items':item_names, 'form': form,},
    )

@login_required(login_url='/nugget/')
def shop(request):
    """
    View function for shop page.
    """
    #User Properties
    usr_id = Profile.objects.get(usr=request.user)
    user = usr_id.usr
    nugget = Nugget.objects.get(user=usr_id)
    coins = usr_id.coins
    nug_attributes = nugget.attributes

    if nugget.name is "":
        return redirect('create')

    # Shop Inventory Logic
    items_shop = Item.objects.all()
    shop_item_names_food = [None]
    shop_item_names_accesory = [None]
    shop_item_names_toy = [None]
    for i in items_shop:
        temp = i.item_status
        attributeToChange = i.item_features
        if attributeToChange == 'he':
            attributeToChange = "Health"
        elif attributeToChange == 'hun':
            attributeToChange = "Hunger"
        elif attributeToChange == 'def':
            attributeToChange = "Defense"
        elif attributeToChange == 'f':
            attributeToChange = "Fatigue"
        elif attributeToChange == 'i':
            attributeToChange = "Intelligence"
        elif attributeToChange == 'happ':
            attributeToChange = "Happiness"
        elif attributeToChange == 'l':
            attributeToChange = "Luck"
        else:
            attributeToChange = "Unknown."

        if temp == "food":
            shop_item_names_food = shop_item_names_food + [i.name, i.price, attributeToChange, i.effect]
        elif temp == "accesory":
            shop_item_names_accesory = shop_item_names_accesory + [i.name, i.price, attributeToChange, i.effect]
        elif temp == "toy":
            shop_item_names_toy = shop_item_names_toy + [i.name, i.price, attributeToChange, i.effect]
    shop_item_names_food = shop_item_names_food[1:]
    if shop_item_names_food == [None]:
        shop_item_names_food = "None"
    shop_item_names_accesory = shop_item_names_accesory[1:]
    if shop_item_names_accesory == [None]:
        shop_item_names_accesory = "None"
    shop_item_names_toy = shop_item_names_toy[1:]
    if shop_item_names_toy == [None]:
        shop_item_names_toy = "None"

    # User Inventory Logic
    inventory = Inventory.objects.get(user=usr_id)
    items_inventory = InventoryItems.objects.filter(inventory=inventory)
    inv_item_names = []
    for i in items_inventory:
        currItem = Item.objects.get(name=i.item.name)
        inv_item_names.append([currItem.name, i.quantity])
    if inv_item_names == []:
        inv_item_names = "None"

    # Form Logic
    if request.method == 'POST':
        if request.POST['action'] == 'selling':
            inventory_form = InventoryFormShop(request.POST, instance=inventory)
            itemToUpdate = request.POST.get('item_id', None)
            if inventory_form.is_valid():
                inventory_form.save()
                quantityToUpdate = inventory_form.cleaned_data.get('ItemQuantity')
                # Removes Items From Inventory
                for i in items_inventory:
                    currentItem = Item.objects.get(name=i.item.name)
                    if currentItem.name == itemToUpdate:
                        objectToUpdate = InventoryItems.objects.get(inventory=inventory, item=currentItem)
                        if objectToUpdate.quantity - quantityToUpdate >= 0:
                            objectToUpdate.quantity -= quantityToUpdate
                            objectToUpdate.save()
                        else:
                            return redirect('shop')
                if objectToUpdate.quantity <= 0:
                    objectToUpdate.delete()
                priceOfTheItem = Item.objects.get(name=itemToUpdate).price
                amountToAddToCoins = priceOfTheItem * quantityToUpdate
                usr_id.coins += amountToAddToCoins
                usr_id.save()
                # We dont really care about discard, it just removes the item anyways.
                #if whatToDoWithItem == 'discard':
                #    return render_to_response('errortemp_2.html', {'val': whatToDoWithItem})
            return redirect('shop')
        if request.POST['action'] == 'buying':
            shop_form = ShopPurchase(request.POST, instance=inventory)
            itemToUpdate = request.POST.get('item_id', None)
            if shop_form.is_valid():
                shop_form.save()
                quantityToUpdate = shop_form.cleaned_data.get('ItemQuantity')
                # Adds Items To Inventory
                found = 0
                if items_inventory[0] == None:
                        theItem = Item.objects.get(name=itemToUpdate)
                        priceOfTheItem = theItem.price
                        amountToRemoveFromCoins = priceOfTheItem * quantityToUpdate
                        if usr_id.coins - amountToRemoveFromCoins > 0:
                            usr_id.coins -= amountToRemoveFromCoins
                            usr_id.save()
                            InventoryItems.objects.create(inventory=inventory,item=theItem,quantity=quantityToUpdate)
                else:
                    for i in items_inventory:
                        currentItem = Item.objects.get(name=i.item.name)
                        if currentItem.name == itemToUpdate:
                            found = 1
                            objectToUpdate = InventoryItems.objects.get(inventory=inventory, item=currentItem)
                            priceOfTheItem = Item.objects.get(name=itemToUpdate).price
                            amountToRemoveFromCoins = priceOfTheItem * quantityToUpdate
                            if usr_id.coins - amountToRemoveFromCoins > 0:
                                usr_id.coins -= amountToRemoveFromCoins
                                usr_id.save()
                                objectToUpdate.quantity += quantityToUpdate
                                objectToUpdate.save()
                    if found == 0:
                        theItem = Item.objects.get(name=itemToUpdate)
                        priceOfTheItem = theItem.price
                        amountToRemoveFromCoins = priceOfTheItem * quantityToUpdate
                        if usr_id.coins - amountToRemoveFromCoins > 0:
                            usr_id.coins -= amountToRemoveFromCoins
                            usr_id.save()
                            InventoryItems.objects.create(inventory=inventory,item=theItem,quantity=quantityToUpdate)
            return redirect('shop')
    else:
        inventory_form = InventoryFormShop()
        shop_form = ShopPurchase()



    return render(
        request,
        'shop.html',
        {'coins':coins, 'shop_items_food':shop_item_names_food, 'shop_items_accesory':shop_item_names_accesory, 'shop_items_toy':shop_item_names_toy,
        'inventory_items':inv_item_names, 'inventory_form':inventory_form, 'shop_form':shop_form}
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

    shape = getattr(nug_attributes, 'nugget_status')

    if shape == 'c':
        size_w = 200
        size_h = 200
    else:
        size_w = 160
        size_h = 200
    eye_size_h = getattr(nug_attributes, 'eye_size')
    eye_size_w = eye_size_h*0.75

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
        opponent_id1 = getattr(i, 'opp_a')
        opponent_id2 = getattr(i, 'opp_b')
        if opponent_id1 == usr_id:
            opponent_id = opponent_id1
        else:
            opponent_id = opponent_id2
        opponent_name = getattr(Nugget.objects.get(user=opponent_id), 'name')
        winner = i.winner
        net_coins = i.net_coins
        won_status = "Lost!"
        if winner == usr_id:
            won_status = "Won!"
            coinStr = "+" + str(net_coins)
        else:
            coinStr = "-" + str(net_coins)
        if battles_list[0] == None:
            battles_list = [[opponent_name, str(coinStr), won_status]]
        else:
            battles_list = battles_list + [[opponent_name, coinStr, won_status]]
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

    active = getattr(battle_set, 'current')

    currBattle = getattr(battle_set, 'activeBattle')
    opponent = None # Profile opponent
    opp = None # Nugget of opponent
    oppAtt = None # Nugget attributes of opponent
    size_w_opp = 160
    size_h_opp = 200
    eye_size_h_opp = 15
    eye_size_w_opp = 12

    if request.method == 'POST':
        if active == 0: # no battles. you send someone a battle
            battleForm = NewBattle(request.POST, user=thisUser)
            if battleForm.is_valid():
                b = battleForm.save()
                user_battles = Battle.objects.get(user=usr_id)
                user_battles.current = 1
                user_battles.activeBattle = b
                user_battles.save()
                their_battles = Battle.objects.get(user=b.opp_b)
                their_battles.current = 3
                their_battles.activeBattle = b
                their_battles.save()
                currBattle = b
                opp = Nugget.objects.get(user=b.opp_b)
                oppAtt = getattr(opp, 'attributes')
                if oppAtt.nugget_status == 'c':
                    size_w_opp = 200
                    size_h_opp = 200
                eye_size_h_opp = oppAtt.eye_size
                eye_size_w_opp = eye_size_h_opp*0.75
                return redirect('battle')
        elif active == 2: # a battle is finished and we're done looking at the results
            battleForm = BattleReset(request.POST, instance=(Battle.objects.get(user=usr_id)))
            if battleForm.is_valid():
                battleForm.save()
            return redirect('battle')
        elif active == 3: # someone sent you a battle and you are responding. if you receive, you're always opp B
            battleForm = BattleResponse(request.POST, instance=(Battle.objects.get(user=usr_id)))
            b = battleForm.save()
            user_battles = Battle.objects.get(user=usr_id)
            thisBattle = getattr(user_battles, 'activeBattle')
            opponent = thisBattle.opp_a
            their_battles = Battle.objects.get(user=opponent)
            opp = Nugget.objects.get(user=opponent)
            oppAtt = getattr(opp, 'attributes')
            if oppAtt.nugget_status == 'c':
                size_w_opp = 200
                size_h_opp = 200
            eye_size_h_opp = oppAtt.eye_size
            eye_size_w_opp = eye_size_h_opp*0.75
            currBattle = b

            if b.current == 2: # you responded yes
                myPts = 0
                urPts = 0

                if nug_attributes.health > oppAtt.health:
                    myPts += 3
                    urPts += 2
                elif nug_attributes.health == oppAtt.health:
                    myPts += 3
                    urPts += 3
                else:
                    myPts += 2
                    urPts += 3
                if nug_attributes.hunger > oppAtt.hunger:
                    myPts += 1
                elif nug_attributes.hunger == oppAtt.health:
                    myPts += 1
                    urPts += 1
                else:
                    urPts += 1
                if nug_attributes.defense > oppAtt.defense:
                    myPts += 3
                    urPts += 2
                elif nug_attributes.defense == oppAtt.defense:
                    myPts += 3
                    urPts += 3
                else:
                    myPts += 2
                    urPts += 3
                if nug_attributes.fatigue > oppAtt.fatigue:
                    myPts += 1
                elif nug_attributes.fatigue == oppAtt.fatigue:
                    myPts += 1
                    urPts += 1
                else:
                    urPts += 0
                if nug_attributes.intelligence > oppAtt.intelligence:
                    myPts += 4
                    urPts += 2
                elif nug_attributes.intelligence == oppAtt.intelligence:
                    myPts += 4
                    urPts += 4
                else:
                    myPts += 2
                    urPts += 4
                if nug_attributes.happiness > oppAtt.happiness:
                    urPts -= 1
                elif nug_attributes.happiness == oppAtt.happiness:
                    myPts += 1
                    urPts += 1
                else:
                    myPts -= 2
                if nug_attributes.luck > oppAtt.luck:
                    myPts += randint(0, 10)
                    urPts += randint(0, 5)
                elif nug_attributes.luck == oppAtt.luck:
                    myPts += randint(0, 10)
                    urPts += randint(0, 10)
                else:
                    myPts += randint(0, 5)
                    urPts += randint(0, 10)

                if myPts == urPts: # choose a random winner
                    choose = randint(0, 1)
                    if choose == 0:
                        myPts += 1
                        nug_attributes.luck += 5
                    else:
                        urPts += 1
                        oppAtt.luck += 5

                if myPts > urPts: # you win
                    currBattle.winner = usr_id
                    nug_attributes.health -= randint(0, 5)
                    nug_attributes.hunger -= randint(10, 20)
                    nug_attributes.defense -= randint(5, 10)
                    nug_attributes.battle_XP += randint(10, 15)
                    nug_attributes.fatigue -= randint(5, 10)
                    nug_attributes.happiness += randint(5, 10)
                    oppAtt.health -= randint(5, 15)
                    oppAtt.hunger -= randint(20, 30)
                    oppAtt.defense -= randint(10, 20)
                    oppAtt.battle_XP += randint(5, 10)
                    oppAtt.fatigue -= randint(10, 15)
                    oppAtt.intelligence -= randint(0, 2)
                    oppAtt.happiness -= randint(10, 20)
                    coins = randint(25, 100)
                    currBattle.net_coins = coins
                    usr_id.coins += coins
                    opponent.coins -= coins
                else: # you lose
                    currBattle.winner = opponent
                    oppAtt.health -= randint(0, 5)
                    oppAtt.hunger -= randint(10, 20)
                    oppAtt.defense -= randint(5, 10)
                    oppAtt.battle_XP += randint(10, 15)
                    oppAtt.fatigue -= randint(5, 10)
                    oppAtt.happiness += randint(5, 10)
                    nug_attributes.health -= randint(5, 15)
                    nug_attributes.hunger -= randint(20, 30)
                    nug_attributes.defense -= randint(10, 20)
                    nug_attributes.battle_XP += randint(5, 10)
                    nug_attributes.fatigue -= randint(10, 15)
                    nug_attributes.intelligence -= randint(0, 2)
                    nug_attributes.happiness -= randint(10, 20)
                    coins = randint(25, 100)
                    currBattle.net_coins = coins
                    usr_id.coins -= coins
                    opponent.coins += coins

                nug_attributes.save()
                oppAtt.save()
                currBattle.save()

                user_battles.battles.add(thisBattle)
                user_battles.save()
                their_battles.battles.add(thisBattle)
                their_battles.current = 2
                their_battles.save()



            else: # you responded no
                user_battles.activeBattle = None
                their_battles.activeBattle = None
                their_battles.current = 0
                thisBattle.delete()
                user_battles.save()
                their_battles.save()
            return redirect('battle')

        else: # you are pending a response
            battleForm = None

    else:

        if active == 0: # no battles
            battle_set.activeBattle = None
            battle_set.save()
            battleForm = NewBattle(user=thisUser, initial={'opp_a': usr_id, })
        elif active == 2: # a battle is finished
            battleForm = BattleReset(initial={'current': 0, })
            opponent = currBattle.opp_a
            opp = Nugget.objects.get(user=opponent)
            oppAtt = getattr(opp, 'attributes')
            if oppAtt.nugget_status == 'c':
                size_w_opp = 200
                size_h_opp = 200
            eye_size_h_opp = oppAtt.eye_size
            eye_size_w_opp = eye_size_h_opp*0.75
        elif active == 3: # someone sent you a battle
            battleForm = BattleResponse()
            opponent = currBattle.opp_a
            opp = Nugget.objects.get(user=opponent)
            oppAtt = getattr(opp, 'attributes')
            if oppAtt.nugget_status == 'c':
                size_w_opp = 200
                size_h_opp = 200
            eye_size_h_opp = oppAtt.eye_size
            eye_size_w_opp = eye_size_h_opp*0.75
        else: # a battle is pending
            battleForm = None
            opponent = currBattle.opp_b
            opp = Nugget.objects.get(user=opponent)
            oppAtt = getattr(opp, 'attributes')
            if oppAtt.nugget_status == 'c':
                size_w_opp = 200
                size_h_opp = 200
            eye_size_h_opp = oppAtt.eye_size
            eye_size_w_opp = eye_size_h_opp*0.75

    return render(
        request,
        'battle.html',
        {'coins':coins, 'nugget':nugget, 'health':health, 'health_color':health_color, 'hunger':hunger, 'hunger_color':hunger_color, 'size_w': size_w, 'size_h': size_h,
        'happiness':happiness, 'happiness_color':happiness_color, 'battle_XP':battle_XP, 'battle_XP_color':battle_XP_color, 'opponents':list_friends, 'eye_size_w': eye_size_w, 'eye_size_h': eye_size_h,
        'color':color, 'mouth':mouth, 'battles':battles_list, 'battleForm': battleForm, 'active': active, 'currBattle': currBattle, 'opp': opp, 'oppAtt': oppAtt, 'size_w_opp': size_w_opp, 'size_h_opp': size_h_opp,
        'eye_size_h_opp': eye_size_h_opp, 'eye_size_w_opp': eye_size_h_opp, },
    )

@login_required(login_url='/nugget/')
def create(request):
    """
    View function for create page.
    """
    usr_id = Profile.objects.get(usr=request.user)
    rec = Nugget.objects.get(user=usr_id)
    att = rec.attributes

    # Remove this when editing the create page.
    if rec.name is not "":
        return redirect('home')

    if request.method == 'POST':
        n1 = CreateNugget(request.POST, instance=rec)
        n2 = CreateAttributes(request.POST, instance=att)
        if n1.is_valid() and n2.is_valid():
            n1.save()
            n2.save()
            attributesOfUser = rec.attributes
            color = n2.cleaned_data.get('color')
            if color == "honeydew":
                attributesOfUser.happiness = 0
            elif color == "goldenrod":
                attributesOfUser.happiness = 10
            elif color == "dark goldenrod":
                attributesOfUser.happiness = 20
            elif color == "sienna":
                attributesOfUser.happiness = 30
            elif color == "burlywood":
                attributesOfUser.happiness = 40
            elif color == "tan":
                attributesOfUser.happiness = 50
            elif color == "coral":
                attributesOfUser.happiness = 60
            elif color == "cyan":
                attributesOfUser.happiness = 80
            elif color == "sky blue":
                attributesOfUser.happiness = 100

            eye_size = n2.cleaned_data.get('eye_size')
            if eye_size < 16:
                attributesOfUser.defense = 100
            elif eye_size < 18:
                attributesOfUser.defense = 70
            elif eye_size < 20:
                attributesOfUser.defense = 50
            elif eye_size < 22:
                attributesOfUser.defense = 40
            elif eye_size < 24:
                attributesOfUser.defense = 30
            elif eye_size < 26:
                attributesOfUser.defense = 20
            elif eye_size < 28:
                attributesOfUser.defense = 10
            elif eye_size < 30:
                attributesOfUser.defense = 0

            nugget_status = n2.cleaned_data.get('nugget_status')
            if nugget_status == "e":
                attributesOfUser.fatigue = 40
            elif nugget_status == "c":
                attributesOfUser.fatigue = 80

            mouth_status = n2.cleaned_data.get('mouth_status')
            if mouth_status == "happy":
                attributesOfUser.intelligence = 20
                attributesOfUser.luck = 80
            elif mouth_status == "nervous":
                attributesOfUser.intelligence = 80
                attributesOfUser.luck = 40
            elif mouth_status == "hungry":
                attributesOfUser.intelligence = 60
                attributesOfUser.luck = 60
            elif mouth_status == "content":
                attributesOfUser.intelligence = 40
                attributesOfUser.luck = 30

            attributesOfUser.save()
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

def help(request):
    """
    View function for help page.
    """
    usr_id = Profile.objects.get(usr=request.user)
    coins = getattr(usr_id, 'coins')
    return render(
        request,
        'help.html',
        {'coins': coins, },
    )

def myaccount(request):
    """
    View function for myaccount page.
    """
    usr_id = Profile.objects.get(usr=request.user)
    coins = getattr(usr_id, 'coins')
    nugget = Nugget.objects.get(user=usr_id)
    user = getattr(usr_id, 'usr')
    userbday = usr_id.bday

    thisUser = request.user
    if hasattr(thisUser, '_wrapped') and hasattr(thisUser, '_setup'):
        if thisUser._wrapped.__class__ == object:
            thisUser._setup()
        thisUser = thisUser._wrapped

    userobject = User.objects.get(id=thisUser.id)
    firstname = userobject.first_name
    lastname = userobject.last_name
    useremail = userobject.email
    username = userobject.username

    return render(
        request,
        'myaccount.html',
        {'coins': coins, 'nugget':nugget, 'user':user, 'userbday':userbday, 'firstname':firstname, 'lastname':lastname, 'useremail':useremail, 'username': username},
    )

# HTTP Error 400
def bad_request(request):
    response = render_to_response('400.html',context_instance=RequestContext(request))

    response.status_code = 400

    return response

# HTTP Error 403
def server_error(request):
    response = render_to_response('403.html',context_instance=RequestContext(request))

    response.status_code = 403

    return response

# HTTP Error 404
def page_not_found(request):
    response = render_to_response('404.html',context_instance=RequestContext(request))

    response.status_code = 404

    return response

# HTTP Error 500
def server_error(request):
    response = render_to_response('500.html',context_instance=RequestContext(request))

    response.status_code = 500

    return response
