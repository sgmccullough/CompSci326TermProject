from django.db import models

# Create your models here.
class User(models.Model):
    """
    Model representing a User Account.
    """
    #Fields
    nug_id = models.IntegerField(help_text="Nugget ID unique to User")
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
        return '%s (%s)' % (self.usr, self.nug_id)
