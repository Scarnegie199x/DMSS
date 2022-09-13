from django.forms import ModelForm
from django import forms

from .models import WeaponItem, ArmorItem, PotionItem,SpellItem,WonderousItem


class WeaponCreationForm(forms.ModelForm):

    class Meta:
        model = WeaponItem
        fields = ['name', 'description', 'price', 'islegendary','attunement', 'category', 'attack', 'damagetype',
                  'weapontype','damage','bonus','properties']


class ArmorCreationForm(forms.ModelForm):

        class Meta:
            model = ArmorItem
            fields = ['name', 'armorclass', 'description', 'price', 'islegendary','attunement', 'category', 'armortype',
                      'weightdisadvantage', 'bonus','properties']

class SpellCreationForm(forms.ModelForm):

        class Meta:
            model = SpellItem
            fields = ['name', 'spell_level','school','casting_time','range','target','components','duration','price',
                      'description', 'higher_levels','spell_lists']

class PotionCreationForm(forms.ModelForm):

        class Meta:
            model = PotionItem
            fields = ['name','description','price', 'properties']

class WonderousCreationForm(forms.ModelForm):
        class Meta:
            model = WonderousItem
            fields = ['name','description','islegendary','price','properties']


