from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventory, Item, Nug_IDs, FriendsList, Battle, BattleInstance, Shop

class BattleInstanceInline(admin.TabularInline):
    model = BattleInstance

class ItemInline(admin.TabularInline):
    model = Item

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'usr', 'email', 'pswd', 'bday', 'coins')
    fields = ['id', 'usr', 'email', 'pswd', 'bday', 'coins']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [ItemInline]

@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [BattleInstanceInline]

admin.site.register(Nug_IDs)
admin.site.register(User, UserAdmin)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(FriendsList)
admin.site.register(BattleInstance)
