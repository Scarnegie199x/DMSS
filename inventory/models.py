from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model

class SharedInfo(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class WeaponItem(SharedInfo):

    DamageType = [
        ('slashing','Slashing'),
        ('bludgeoning','Bludgeoning'),
        ('piercing', "Piercing"),
    ]
    CategoryType = [
        ('simple', 'Simple'),
        ('martial', 'Martial'),
    ]
    AttackType = [
        ('melee', 'Melee'),
        ('ranged', 'Ranged'),
    ]

    islegendary = models.BooleanField(default=False, verbose_name="Legendary")
    attunement = models.BooleanField(default=False)
    category = models.CharField(blank=False, choices=CategoryType, max_length=10)
    attack = models.CharField(blank=False, choices=AttackType, max_length=10)
    damagetype = models.CharField(blank=False, choices=DamageType, max_length=20, verbose_name="Damage type")
    weapontype = models.CharField(blank=False, choices=None, max_length=20, verbose_name="Weapon type")
    damage = models.CharField(max_length=8, blank=False)
    bonus = models.CharField(max_length=3, blank=False)
    properties = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("weapon_detail", args=[str(self.id)])

class ArmorItem(SharedInfo):

    CategoryType = [
        ('heavy','Heavy'),
        ('medium', 'Medium'),
        ('light', 'Light'),
    ]

    islegendary = models.BooleanField(default=False, verbose_name="Legendary")
    weightdisadvantage = models.BooleanField(default=False, verbose_name="Weight Disadvantage")
    attunement = models.BooleanField(default=False)
    category =  models.CharField(blank=False, choices = CategoryType, max_length=15)
    armorclass = models.IntegerField(verbose_name="AC")
    armortype = models.CharField(blank=False, choices=None, max_length=15, verbose_name="Armor type")
    bonus = models.CharField(max_length=3)
    properties = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("armor_detail", args=[str(self.id)])

class WonderousItem(SharedInfo):
    islegendary = models.BooleanField(default=False, verbose_name="Legendary")

    def get_absolute_url(self):
        return reverse("wonderous_detail", args=[str(self.id)])
    def __str__(self):
        return self.name


class PotionItem(SharedInfo):

    def get_absolute_url(self):
        return reverse("potion_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

class SpellItem(SharedInfo):

    spell_level = models.CharField(max_length=10, blank=False, verbose_name="Spell level")
    school = models.CharField(max_length = 50)
    casting_time = models.CharField(max_length=50, verbose_name="Casting time")
    range = models.CharField(max_length=50)
    target = models.CharField(max_length=50, blank=False)
    components = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    higher_levels = models.CharField(max_length=200, verbose_name="Higher level cast")
    spell_lists = models.CharField(max_length=100,verbose_name="Spell list")

    def get_absolute_url(self):
        return reverse("spell_detail", args=[str(self.id)])

    def __str__(self):
        return self.name
