from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventorie, Shop, Item, Battle, Nug_IDs, FriendsList, Battle

admin.site.register(User)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Inventorie)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Nug_IDs)
admin.site.register(FriendsList)
admin.site.register(Battle)
