from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventorie, Shop, Item

admin.site.register(User)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Inventorie)
admin.site.register(Shop)
admin.site.register(Item)
