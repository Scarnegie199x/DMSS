from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView


from .forms import CustomUserCreationForm
from .models import CustomUser
from inventory.models import WeaponItem, ArmorItem, PotionItem, SpellItem,WonderousItem
from inventory.forms import WeaponCreationForm, ArmorCreationForm,SpellCreationForm,WonderousCreationForm,PotionCreationForm


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "account/editprofile.html"
    fields = ['email', 'dungeon_name', 'username']
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "account/signup.html"

class UserPageView(DetailView):

    model = CustomUser
    template_name = "user/user.html"
    context_object_name = "userpage"

    def get_context_data(self, *args, **kwargs):
        #Gather data on the items the author has created on their own URL
        context = super(UserPageView, self).get_context_data(*args, **kwargs)
        userpage = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        context['user_weapon'] = WeaponItem.objects.filter(author__username__icontains=userpage)
        context['user_armor'] = ArmorItem.objects.filter(author__username__icontains=userpage)
        context['user_spell'] = SpellItem.objects.filter(author__username__icontains=userpage)
        context['user_potion'] = PotionItem.objects.filter(author__username__icontains=userpage)
        context['user_wonderous'] = WonderousItem.objects.filter(author__username__icontains=userpage)
        return context

    def get_object(self):
        #get_object to collect data on the users detailed page
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        return object


