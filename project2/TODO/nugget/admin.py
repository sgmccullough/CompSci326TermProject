from django.contrib import admin

# Register your models here.
from .models import User, Nugget, NuggetAttribute, Inventorie

admin.site.register(User)
admin.site.register(Nugget)
admin.site.register(NuggetAttribute)
admin.site.register(Inventorie)
