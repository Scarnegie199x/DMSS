from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import WeaponCreationForm, ArmorCreationForm, SpellCreationForm, PotionCreationForm, WonderousCreationForm
from .models import WeaponItem, ArmorItem, PotionItem, SpellItem, WonderousItem
from accounts.models import CustomUser

class WeaponCreateView(LoginRequiredMixin,CreateView):
    model = WeaponItem
    template_name = "inventory/new_weapon.html"
    form_class = WeaponCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArmorCreateView(LoginRequiredMixin, CreateView):
    model = ArmorItem
    template_name = "inventory/new_armor.html"
    form_class = ArmorCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SpellCreateView(LoginRequiredMixin, CreateView):
    model = SpellItem
    template_name = "inventory/new_spell.html"
    form_class = SpellCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PotionCreateView(LoginRequiredMixin, CreateView):
    model = PotionItem
    template_name = "inventory/new_potion.html"
    form_class = PotionCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WonderousCreateView(LoginRequiredMixin, CreateView):
    model = WonderousItem
    template_name = "inventory/new_wonderous.html"
    form_class = WonderousCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ItemListView(TemplateView):
    template_name = "inventory/item_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_model()
        context['weaponlist'] = WeaponItem.objects.all()
        context['potionlist'] = PotionItem.objects.all()
        context['armorlist'] = ArmorItem.objects.all()
        context['spelllist'] = SpellItem.objects.all()
        context['wonderlist'] = WonderousItem.objects.all()
        return context



class WeaponDetailView(DetailView):
    model = WeaponItem
    template_name = "inventory/weapon_detail.html"
    context_object_name = 'weapon'

class ArmorDetailView(DetailView):
    model = ArmorItem
    template_name = "inventory/armor_detail.html"
    context_object_name = 'armor'

class PotionDetailView(DetailView):
    model = PotionItem
    template_name = "inventory/potion_detail.html"
    context_object_name = 'potion'

class SpellDetailView(DetailView):
    model = SpellItem
    template_name = "inventory/spell_detail.html"
    context_object_name = 'spell'

class WonderousDetailView(DetailView):
    model = WonderousItem
    template_name = "inventory/wonderous_detail.html"
    context_object_name = 'wonderous'

class UpdateWeaponView(UpdateView):
    model = WeaponItem
    template_name = "inventory/update.html"
    fields = ['name', 'description', 'price', 'islegendary','attunement', 'category', 'attack', 'damagetype',
                  'weapontype','damage','bonus','properties']

class UpdateArmorView(UpdateView):
    model = ArmorItem
    template_name = "inventory/update.html"
    fields = ['name', 'armorclass', 'description', 'price', 'islegendary','attunement', 'category', 'armortype',
                      'weightdisadvantage', 'bonus','properties']

class UpdatePotionView(UpdateView):
    model = PotionItem
    template_name = "inventory/update.html"
    fields = ['name', 'description', 'price']

class UpdateSpellView(UpdateView):
    model = SpellItem
    template_name = "inventory/update.html"
    fields = ['name', 'spell_level', 'school', 'casting_time', 'range', 'target', 'components', 'duration', 'price',
              'description', 'higher_levels', 'spell_lists']

class UpdateWonderousView(UpdateView):
    model = WonderousItem
    template_name = "inventory/update.html"
    fields = ['name', 'description', 'islegendary', 'price']