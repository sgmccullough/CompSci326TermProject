from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventorie, Shop, Item, battle, nug_ids, friends_list

admin.site.register(User)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Inventorie)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(battle)
admin.site.register(nug_ids)
admin.site.register(friends_list)
