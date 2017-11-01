from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventory, Item, Friend, Battle, BattleInstance, Shop, InventoryItems


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'usr', 'email', 'pswd', 'bday', 'coins')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')

@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'item_status', 'item_features')

@admin.register(InventoryItems)
class InventoryItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'inventory')

@admin.register(BattleInstance)
class BattleInstanceAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Nug_IDs)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Shop)
admin.site.register(Friend)
