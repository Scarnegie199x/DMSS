from django.contrib import admin
from .models import WeaponItem, ArmorItem, WonderousItem, SpellItem, PotionItem


admin.register(WeaponItem,ArmorItem,WonderousItem,SpellItem,PotionItem)(admin.ModelAdmin)

