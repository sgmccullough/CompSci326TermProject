from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Profile(models.Model):
    """
    Model representing a User Account.
    """
    #Fields
    id = models.UUIDField(verbose_name="ID", default=uuid.uuid4, primary_key=True, help_text="ID")
    usr = models.OneToOneField(User, on_delete=models.CASCADE)
    bday = models.DateField(verbose_name="Birthday", auto_now=False, default=datetime.date.today)
    coins = models.IntegerField(verbose_name="Coins", help_text="User Currency", default=500)
    last_login_date = models.DateField(verbose_name="Last Login Date", auto_now=False, default=datetime.date.today)

    #Metadeta
    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"
        ordering = ["id", "usr", "bday", "coins", "last_login_date"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of User
        """
        return reverse('profile-detail', args=[str(self.usr)])

    def __str__(self):
        """
        String for representing the User object (in Admin site)
        """
        return str(self.usr)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usr=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Nugget(models.Model):
    """
    Model representing a Nugget.
    """
    #Fields
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="Name", max_length=25, help_text="Nugget name", default="")
    attributes = models.ForeignKey('NuggetAttribute', null=False, verbose_name="Attributes")
    inventory = models.ForeignKey('Inventory', null=False, verbose_name="Inventory")

    #Metadeta
    class Meta:
        verbose_name = "Nugget"
        ordering = ["name"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Nugget
        """
        return reverse('nugget-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Nugget
        """
        return str(self.name)


class NuggetAttribute(models.Model):
    """
    Model representing a Nugget's Attributes.
    """
    #Fields
    id = models.UUIDField(verbose_name="ID", default=uuid.uuid4, primary_key=True, help_text="ID")
    health = models.IntegerField(verbose_name="Health", help_text="Nugget Health", default=100)
    color = models.CharField(verbose_name="Color", max_length =50, help_text="Nugget Color", default="goldenrod")
    eye_size = models.IntegerField(verbose_name="Eye Size", help_text="Eye size", default=10)
    experience = models.IntegerField(verbose_name="XP", help_text="Experience Points", default=0)
    hunger = models.IntegerField(verbose_name="Hunger", help_text="Nugget Hunger", default=100)
    happiness = models.IntegerField(verbose_name="Happiness", help_text="Nugget Happiness", default=100)
    defense = models.IntegerField(verbose_name="Defense", help_text="Nugget Defense", default=100)
    battle_XP = models.IntegerField(verbose_name="Battle XP", help_text="Battle Experience Points", default=0)
    fatigue = models.IntegerField(verbose_name="Fatigue", help_text="Nugget Fatigue", default=100)
    intelligence = models.IntegerField(verbose_name="Intelligence", help_text="Nugget Intelligence", default=20)
    luck = models.IntegerField(verbose_name="Luck", help_text="Nugget Luck", default=20)

    mouth_type = (
        ('hyper', 'Hyper'),
        ('nervous', 'Nervous'),
        ('hungry', 'Hungry'),
        ('content', 'Content'),
    )

    nugget_shape = (
        ('e', 'Egg'),
        ('c', 'Circle'),
    )

    mouth_status = models.CharField(max_length=10, choices=mouth_type, blank=True, default='h', help_text='Type of Nugget Mouth')
    #eye_status = models.CharField(max_length=10, choices=eye_shape, blank=True, default='w', help_text='Type of Nugget Eye')
    nugget_status = models.CharField(max_length=10, choices=nugget_shape, blank=True, default='e', help_text='Type of Nugget Shape')

    #Metadata
    class Meta:
        verbose_name = "Nugget Attributes"
        verbose_name_plural = "Nugget Attributes"
        ordering = ["nugget_status", "experience"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of nugget attributes
        """
        return reverse('nugget-attributes-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Nugget attributes
        """
        return str(self.id)

class Item(models.Model):
    """
    Model representing an item
    """
    #Fields
    id = models.UUIDField(verbose_name="Item ID", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this item")
    name = models.CharField(verbose_name="Item Name", max_length=25, help_text = "Name of item")
    price = models.IntegerField(verbose_name="Price", help_text="Item Price", default=5)
    effect = models.IntegerField(verbose_name="+/- Stat", help_text="+/- Stat1", default=5)
    effect2 = models.IntegerField(verbose_name="+/- Stat", help_text="+/- Stat2", default=5, null=True)
    desc = models.CharField(verbose_name="Item Description", max_length=100, help_text="Item Description", default="")

    item_type = (
        ('food', 'Food'),
        ('accesory', 'Accesories'),
        ('toy', 'Toys')
    )

    item_attribute= (
        ('he', 'Health'),
        ('hun', 'Hunger'),
        ('def', 'Defense'),
        ('f', 'Fatigue'),
        ('i', 'Intelligence'),
        ('happ', 'Happiness'),
        ('l', 'luck')
    )

    item_status = models.CharField(verbose_name="Type", max_length=100, choices=item_type, blank=True, default='c', help_text='Type of Item')
    item_features= models.CharField(verbose_name="Features", max_length=100, choices=item_attribute, blank=True, default='he', help_text='Type of Feature1')
    item_features2 = models.CharField(verbose_name="Features", max_length=100, choices=item_attribute, blank=True, null=True, default='he', help_text='Type of Feature2')

    #Metadata
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["id", "name", "price", "effect", "effect2", "item_status", "item_features", "item_features2"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access items
        """
        return reverse('Item-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing an item
        """
        return str(self.id)


class Inventory(models.Model):
    """
    Model representing a User's Inventory
    """
    #Fields
    id = models.UUIDField(verbose_name="ID", default=uuid.uuid4, primary_key=True, help_text="ID")
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('Item', through='InventoryItems')
    msg = models.CharField(verbose_name="Message Field", max_length=200)
    msg_shop = models.CharField(verbose_name="Message Field", max_length=200, default="")

    #Metadata
    class Meta:
        verbose_name = "User Inventory"
        verbose_name_plural = "User Inventory"
        ordering = ["id"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Inventory
        """
        return reverse('Inventory-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Inventory
        """
        return str(self.id)

class InventoryItems(models.Model):
    """
    Model representing the quantity of a given item in a user's inventory. Implemented as a through table/
    """

    inventory = models.ForeignKey('Inventory')
    item = models.ForeignKey('Item')
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Inventory Through Data"
        verbose_name_plural = "Inventory Through Data"

class Shop(models.Model):
    """
    Model representing the Shop
    """

    items = models.ManyToManyField('Item')
    msg = models.CharField(verbose_name="Message Field", max_length=200)

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access the shop
        """
        return reverse('Shop-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Shop
        """
        return str(self.id)

class Battle(models.Model):
    """
    Model representing all of a user's battles
    """

    battles = models.ManyToManyField('BattleInstance', related_name='list_battles', blank=True, null=True)
    activeBattle = models.ForeignKey('BattleInstance', null=True, blank=True)
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User ID")
    current = models.IntegerField(verbose_name="Status", help_text="Specifies an active battle. 0=inactive, 1=active/pending response, 2=finished, 3=must respond", default='0')

    class Meta:
        verbose_name = "User Battle Set"
        verbose_name_plural = "User Battle Sets"
        ordering = ["id"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access Battle
        """
        return reverse('battle-detail', args=[str(self.user)])

    def __str__(self):
        """
        String for representing a Battle
        """
        return str(self.user)

class BattleInstance(models.Model):
    """
    Model representing a single battle
    """
    #Fields
    id = models.UUIDField(verbose_name="Battle ID", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this battle")
    net_coins = models.IntegerField(verbose_name="Net Coins", default=0, help_text = "Coins won or lost")
    opp_a = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="Opponent", related_name='opponent_A')
    opp_b = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="Opponent", related_name='opponent_B')
    nug_xp= models.IntegerField(verbose_name="Net XP", help_text="Nugget Experience", default='0')
    winner = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="Winner", related_name='Winner')
    stats_a = models.CharField(verbose_name="Stats Changes for Opponent A", max_length=500, default="")
    stats_b = models.CharField(verbose_name="Stats Changes for Opponent B", max_length=500, default="")
    #Metadata
    class Meta:
        verbose_name = "Battle"
        verbose_name_plural = "Battles"
        ordering = ["id", "net_coins", "nug_xp", "opp_a", "opp_b", "stats_a", "stats_b"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access battles
        """
        return reverse('battle-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing a battle
        """
        return str(self.id)

class Friend(models.Model):
    users = models.ManyToManyField('Profile', verbose_name="Friends")
    current_user = models.ForeignKey('Profile', related_name="owner", verbose_name="User", null=True)


    class Meta:
        verbose_name = "Friends List"

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return str(self.current_user)

class News(models.Model):
    text = models.CharField(verbose_name="News Item", max_length=250)

    class Meta:
        ordering = ['text']

    def __str__(self):
        """
        String for representing a News Item
        """
        return str(self.text)

class Chat(models.Model):
    id = models.UUIDField(verbose_name="forum id", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this forum post")
    user1 = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User1 in the chat", related_name='chat_user_1')
    user2 = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User2 in the chat", related_name='chat_user_2')

    class Meta:
        ordering = ['id', 'user1', 'user2']

    def __str__(self):
        """
        String for representing a News Item
        """
        return str(self.id)

class ChatMessage(models.Model):
    chatThread = models.ForeignKey('Chat', on_delete=models.SET_NULL, null=True, verbose_name="link to the chat thread")
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User in the chat corresponding to this message")
    content = models.CharField(verbose_name="content", max_length=200, blank=True, default='None', help_text='message content')
    date = models.DateField(verbose_name="Post Date", auto_now=False, default=datetime.date.today)

    class Meta:
        ordering = ['chatThread', 'user', 'content', 'date']

    def __str__(self):
        """
        String for representing a News Item
        """
        return str(self.chatThread)

class Forum(models.Model):
    id = models.UUIDField(verbose_name="forum id", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this forum post")
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User in the chat")
    topic = models.CharField(verbose_name="subject", max_length=100, blank=True, default='General', help_text='Forum Topic')
    subject = models.CharField(verbose_name="subject", max_length=100, blank=True, default='Subject', help_text='Forum Subject')
    content = models.CharField(verbose_name="content", max_length=1000, blank=True, default='None', help_text='Forum Content')
    date = models.DateField(verbose_name="Post Date", auto_now=False, default=datetime.date.today)
    #private = models.BooleanField(verbose_name="Private Post")
    #allowedusers = models.ManyToManyField('Profile', verbose_name="Allowed Users")

    class Meta:
        ordering = ['id', 'user', 'topic', 'subject', 'content', 'date']

    def __str__(self):
        """
        String for representing a News Item
        """
        return str(self.id)

class ForumComments(models.Model):
    originalPost = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True, verbose_name="link comment to a forum post")
    user = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, verbose_name="User in the chat")
    content = models.CharField(verbose_name="content", max_length=200, blank=True, default='None', help_text='Forum comment content')
    date = models.DateField(verbose_name="Post Date", auto_now=False, default=datetime.date.today)

    class Meta:
        ordering = ['originalPost', 'user', 'content', 'date']

    def __str__(self):
        """
        String for representing a News Item
        """
