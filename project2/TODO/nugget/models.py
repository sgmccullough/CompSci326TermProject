from django.db import models

# Create your models here.
class User(models.Model):
    """
    Model representing a User Account.
    """
    #Fields
    nug_id = models.IntegerField(primary_key=True, help_text="Nugget ID unique to User")
    usr = models.CharField(max_length=25, help_text="Username")
    email = models.EmailField(max_length=50, help_text="User Email")
    pswd = models.CharField(max_length=50, help_text="User Password")
    bday = models.DateField(auto_now=True)
    coins = models.IntegerField(help_text="User Currency")
    #Messages & Settings should be their own models ?

    #Metadeta
    class Meta:
        ordering = ["nug_id", "usr", "email", "pswd", "bday", "coins"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of User
        """
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the User object (in Admin site)
        """
        return str(self.nug_id)


class Nugget(models.Model):
    """
    Model representing a Nugget.
    """
    #Fields
    nug_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=25, help_text="Nugget name")
    inventory = models.ForeignKey('Inventorie', on_delete=models.SET_NULL, null=True)
    attributes = models.ForeignKey('NuggetAttribute', on_delete=models.SET_NULL, null=True)

    #Metadeta
    class Meta:
        ordering = ["nug_id", "name"]

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
    nug_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    nug_health = models.IntegerField(help_text="health of nugget", default=100)
    nug_color = models.CharField(max_length =50, help_text="Nugget color")
    nug_size = models.IntegerField(help_text="Nugget size", default=20)
    mouth_size = models.IntegerField(help_text="Mouth size", default=10)
    eye_size = models.IntegerField(help_text="Eye size", default=10)
    experience = models.IntegerField(help_text="Experience Points", default=50)
    hunger=models.IntegerField(help_text="Nugget Hunger", default=100)
    happiness=models.IntegerField(help_text="Nugget Happiness", default=100)
    defense=models.IntegerField(help_text="Nugget Defense", default=100)
    battle_XP=models.IntegerField(help_text="Battle Experience Points", default=100)
    fatigue=models.IntegerField(help_text="Nugget Fatigue", default=100)
    intelligence=models.IntegerField(help_text="Nugget Intelligence", default=20)
    luck=models.IntegerField(help_text="Nugget Luck", default=20)

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
        ordering = ["nug_id", "mouth_status", "eye_status", "nugget_status", "experience"]

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
        return str(self.nug_id)

class Inventorie(models.Model):
    """
    Model representing Items and Inventory
    """
    #Fields
    item_id = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    inv_id = models.IntegerField(help_text = "Unique Inventory ID")

    #Metadata
    class Meta:
        ordering = ["item_id", "inv_id"]

    #Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Inventory
        """
        return reverse('Inventorie-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Inventory
        """
        return str(self.inv_id)

class Shop(models.Model):
    """
    Model representing the Shop
    """
    #Fields
    item_id = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)

    #Metadata
    class Meta:
        ordering = ["item_id"]

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
        return str(self.item_id)

class Item(models.Model):
    """
    Model representing the items
    """
    #Fields
    item_id = models.IntegerField(help_text = "Unique Item ID")
    item_name = models.CharField(max_length=25, help_text = "Name of item")

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

    item_status = models.CharField(max_length=100, choices=item_type, blank=True, default='c', help_text='Type of Item')
    item_features= models.CharField(max_length=100, choices=item_attribute, blank=True, default='he', help_text='Type of Feature')

    #Metadata
    class Meta:
        ordering = ["item_id", "item_name"]

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
        return str(self.item_id)

class Battle(models.Model):
    """
    Model representing battles
    """
    #Fields
    battle_id = models.IntegerField(help_text="Unique Battle ID")
    nug_id = models.ForeignKey('Nugget', on_delete=models.SET_NULL, null=True)
    net_coins = models.DecimalField(max_digits=10, decimal_places = 0, help_text = "Coins won or lost")
    # inv_id = models.ForeignKey('NuggetInventorie', on_delete=models.SET_NULL, null=True)
    opponent_id = models.ForeignKey('nug_ids', on_delete=models.SET_NULL, null=True)
    nug_xp=models.IntegerField(help_text="Nugget Experience", default='0')
    #Metadata
    class Meta:
        ordering = ["battle_id", "nug_id", "net_coins"]

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
        return str(self.battle_id)

class Nug_IDs(models.Model):
    """
    Model representing all the nugget ids
    """
    #Fields
    nug_id = models.ForeignKey('Nugget', on_delete=models.SET_NULL, null=True)

    #Metadata
    class Meta:
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
    nug_id = models.ForeignKey('Nugget', on_delete=models.SET_NULL, null=True)
    friends = models.IntegerField(db_column="friends")
    added = models.IntegerField(db_column="added_friends")
    pending = models.IntegerField(db_column="pending_friends")

    #Metadata
    class Meta:
        ordering = ["nug_id"]

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
        return str(self.nug_id)
