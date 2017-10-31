from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class User(models.Model):
    """
    Model representing a User Account.
    """
    #Fields
    id = models.UUIDField(verbose_name="ID", primary_key=True, default=uuid.uuid4, help_text="ID")
    usr = models.CharField(verbose_name="Username", max_length=25, help_text="Username")
    email = models.EmailField(verbose_name="Email", max_length=50, help_text="User Email")
    pswd = models.CharField(verbose_name="Password", max_length=50, help_text="User Password")
    bday = models.DateField(verbose_name="Birthday", auto_now=False)
    coins = models.IntegerField(verbose_name="Coins", help_text="User Currency")
    #nugg = models.ForeignKey('Nugget', on_delete=models.SET_NULL, null=True)
    #battles = models.ForeignKey('Battle', on_delete=models.SET_NULL, null=True)
    #friends = models.ForeignKey('FriendsList', on_delete=models.SET_NULL, null=True)
    #inventory = models.ForeignKey('Inventory', on_delete=models.SET_NULL, null=True)

    #Messages & Settings should be their own models ?

    #Metadeta
    class Meta:
        verbose_name = "User"
        ordering = ["id", "usr", "email", "pswd", "bday", "coins"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of User
        """
        return reverse('user-detail', args=[str(self.usr)])

    def __str__(self):
        """
        String for representing the User object (in Admin site)
        """
        return str(self.usr)


class Nugget(models.Model):
    """
    Model representing a Nugget.
    """
    #Fields
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="Name", max_length=25, help_text="Nugget name")
    attributes = models.ForeignKey('NuggetAttribute', null=False, verbose_name="Attributes")
    #friends = models.ManyToManyField('self', through='friend',symmetrical=False,related_name='related_to+')

    #Metadeta
    class Meta:
        verbose_name = "Nugget"
        ordering = ["name"]

    #Methods
    # def add_friend(self, person, status, symm=True):
    #     friend, created = friend.objects.get_or_create(
    #         from_person=self,
    #         to_person=person,
    #         status=status)
    #     if symm: # avoid recursion by passing `symm=False`
    #         person.add_friend(self, status, False)
    #     return friend
    #
    # def remove_friend(self, person, status, symm=True):
    #     friend.objects.filter(
    #         from_person=self,
    #         to_person=person,
    #         status=status).delete()
    #     if symm: # avoid recursion by passing `symm=False`
    #         person.remove_friend(self, status, False)
    #
    # def get_friend(self, status):
    #     return self.friends.filter(
    #         to_people__status=status,
    #         to_people__from_person=self)

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
    health = models.IntegerField(verbose_name="Health", help_text="Nugget Health", default=100)
    color = models.CharField(verbose_name="Color", max_length =50, help_text="Nugget Color")
    nug_size = models.IntegerField(verbose_name="Size", help_text="Nugget size", default=20)
    mouth_size = models.IntegerField(verbose_name="Mouth Size", help_text="Mouth size", default=10)
    eye_size = models.IntegerField(verbose_name="Eye Size", help_text="Eye size", default=10)
    experience = models.IntegerField(verbose_name="XP", help_text="Experience Points", default=50)
    hunger = models.IntegerField(verbose_name="Hunger", help_text="Nugget Hunger", default=100)
    happiness = models.IntegerField(verbose_name="Happiness", help_text="Nugget Happiness", default=100)
    defense = models.IntegerField(verbose_name="Defense", help_text="Nugget Defense", default=100)
    battle_XP = models.IntegerField(verbose_name="Battle XP", help_text="Battle Experience Points", default=100)
    fatigue = models.IntegerField(verbose_name="Fatigue", help_text="Nugget Fatigue", default=100)
    intelligence = models.IntegerField(verbose_name="Intelligence", help_text="Nugget Intelligence", default=20)
    luck = models.IntegerField(verbose_name="Luck", help_text="Nugget Luck", default=20)

    mouth_type = (
        ('h', 'Happy'),
        ('n', 'Nervous'),
        ('d', 'displeased'),
        ('hu', 'Hungry'),
    )

    eye_shape = (
        ('w', 'Wide'),
        ('s', 'Small'),
        ('sl', 'Sleepy'),
        ('m', 'Mad'),
    )

    nugget_shape = (
        ('e', 'Egg-like'),
        ('r', 'Round'),
        ('t', 'Triangle'),
        ('s', 'Square'),
    )

    mouth_status = models.CharField(max_length=1, choices=mouth_type, blank=True, default='h', help_text='Type of Nugget Mouth')
    eye_status = models.CharField(max_length=1, choices=eye_shape, blank=True, default='w', help_text='Type of Nugget Eye')
    nugget_status = models.CharField(max_length=1, choices=nugget_shape, blank=True, default='e', help_text='Type of Nugget Shape')

    #Metadata
    class Meta:
        verbose_name = "Nugget Attributes"
        verbose_name_plural = "Nugget Attributes"
        ordering = ["mouth_status", "eye_status", "nugget_status", "experience"]

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
        return str(self.color)

class Inventory(models.Model):
    """
    Model representing Inventory
    """
    #Fields
    #List of items

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    #Metadata
    class Meta:
        verbose_name = "User Inventory"
        verbose_name_plural = "User Inventory Sets"
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
        return str(self.user.id)

class Shop(models.Model):
    """
    Model representing the Shop
    """
    #Methods
    def get_absolute_url(self):
        """
        REturns the url to access the shop
        """
        return reverse('Shop-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Shop
        """
        return str(self.id)

class Item(models.Model):
    """
    Model representing the items
    """
    #Fields
    id = models.UUIDField(verbose_name="Item ID", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this item")
    name = models.CharField(verbose_name="Item Name", max_length=25, help_text = "Name of item")
    inventory = models.ForeignKey('Inventory', null=True, blank=True)
    shop = models.ForeignKey('Shop')

    item_type = (
        ('a', 'Armor'),
        ('c', 'Consumables')
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
    item_features= models.CharField(verbose_name="Features", max_length=100, choices=item_attribute, blank=True, default='he', help_text='Type of Feature')

    #Metadata
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["id", "name"]

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
        return str(self.name)


class Battle(models.Model):

    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "User Battle Set"
        verbose_name_plural = "User Battle Sets"
        ordering = ["user"]

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
    Model representing battles
    """
    #Fields
    battle = models.ForeignKey('Battle', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(verbose_name="Battle ID", primary_key=True, default=uuid.uuid4, help_text="Unique ID for this battle")
    net_coins = models.DecimalField(verbose_name="Net Coins", max_digits=10, decimal_places = 0, help_text = "Coins won or lost")
    opponent_id = models.ForeignKey('Nug_IDs', on_delete=models.SET_NULL, null=True, verbose_name="Opponent ID")
    nug_xp=models.IntegerField(verbose_name="Net XP", help_text="Nugget Experience", default='0')
    #Metadata
    class Meta:
        verbose_name = "Battle"
        verbose_name_plural = "Battles"
        ordering = ["id", "net_coins"]

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

class Nug_IDs(models.Model):
    # We still need to figure this out.
    """
    Model representing all the nugget ids
    """
    #Fields
    nug_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    friends = models.ForeignKey('FriendsList', on_delete=models.SET_NULL, null=True)

    #Metadata
    class Meta:
        verbose_name = "Nugget ID"
        verbose_name_plural = "Nugget IDs"
        ordering = ["nug_id"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access battles
        """
        return reverse('nudids-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing a battle
        """
        return str(self.nug_id)

class FriendsList(models.Model):
    """
    Model representing a nugget's friends
    """
    #Fields
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    #Metadata
    class Meta:
        verbose_name = "User Friends List"
        verbose_name_plural = "User Friend Lists"
        ordering = ["user"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access battles
        """
        return reverse('friends-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing a battle
        """
        return str(self.user)
