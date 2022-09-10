from django.urls import path


from .views import (
    WeaponCreateView,
    ItemListView,
    WeaponDetailView,
    ArmorDetailView,
    PotionDetailView,
    SpellDetailView,
    WonderousDetailView,
    ArmorCreateView,
    SpellCreateView,
    PotionCreateView,
    WonderousCreateView,
    UpdateWeaponView,
    UpdateArmorView,
    UpdatePotionView,
    UpdateSpellView,
    UpdateWonderousView,
)

urlpatterns = [
    path('weapon/<uuid:pk>/', WeaponDetailView.as_view(), name='weapon_detail'),
    path('armor/<uuid:pk>/', ArmorDetailView.as_view(), name='armor_detail'),
    path('potion/<uuid:pk>/', PotionDetailView.as_view(), name='potion_detail'),
    path('spell/<uuid:pk>/', SpellDetailView.as_view(), name='spell_detail'),
    path('wonderous/<uuid:pk>/', WonderousDetailView.as_view(), name='wonderous_detail'),
    path('item_list/', ItemListView.as_view(), name="item_list"),
    path('new_item/weapon/', WeaponCreateView.as_view(), name="new_weapon"),
    path('new_item/armor/', ArmorCreateView.as_view(), name="new_armor"),
    path('new_item/spell/', SpellCreateView.as_view(), name="new_spell"),
    path('new_item/potion/', PotionCreateView.as_view(), name="new_potion"),
    path('new_item/wonderous/', WonderousCreateView.as_view(), name="new_wonderous"),
    path('weapon/<uuid:pk>/edit/' ,UpdateWeaponView.as_view(), name = "updateweaponitem"),
    path('armor/<uuid:pk>/edit/' ,UpdateArmorView.as_view(), name = "updatearmoritem"),
    path('potion/<uuid:pk>/edit/' ,UpdatePotionView.as_view(), name = "updatepotionitem"),
    path('spell/<uuid:pk>/edit/' ,UpdateSpellView.as_view(), name = "updatespellitem"),
    path('wonderous/<uuid:pk>/edit/' ,UpdateWonderousView.as_view(), name = "updatewonderousitem"),


]