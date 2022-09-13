from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from profanity.validators import validate_is_profane

class SharedInfo(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=100, validators=[validate_is_profane])
    description = models.TextField(validators=[validate_is_profane])
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
    category = models.CharField(blank=False, choices=CategoryType, max_length=10,validators=[validate_is_profane])
    attack = models.CharField(blank=False, choices=AttackType, max_length=10)
    damagetype = models.CharField(blank=False, choices=DamageType, max_length=20, verbose_name="Damage type")
    weapontype = models.CharField(blank=False, choices=None, max_length=20, verbose_name="Weapon type",validators=[validate_is_profane])
    damage = models.CharField(max_length=8, blank=False,validators=[validate_is_profane])
    bonus = models.IntegerField(default=0, validators=[
        MaxValueValidator(9),
        MinValueValidator(0),
    ], blank=False)
    properties = models.CharField(max_length=200,validators=[validate_is_profane])

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
    armortype = models.CharField(blank=False, choices=None, max_length=15, verbose_name="Armor type",validators=[validate_is_profane])
    bonus = models.IntegerField(default=0,validators=[
            MaxValueValidator(9),
            MinValueValidator(0),
        ], blank=False)
    properties = models.CharField(max_length=200,validators=[validate_is_profane])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("armor_detail", args=[str(self.id)])

class WonderousItem(SharedInfo):
    islegendary = models.BooleanField(default=False, verbose_name="Legendary")
    properties = models.CharField(max_length=200, default=False,validators=[validate_is_profane])
    def get_absolute_url(self):
        return reverse("wonderous_detail", args=[str(self.id)])
    def __str__(self):
        return self.name


class PotionItem(SharedInfo):
    properties = models.CharField(max_length=200, default=False,validators=[validate_is_profane])
    def get_absolute_url(self):
        return reverse("potion_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

class SpellItem(SharedInfo):

    spell_level = models.CharField(max_length=10, blank=False, verbose_name="Spell level",validators=[validate_is_profane])
    school = models.CharField(max_length = 50,validators=[validate_is_profane])
    casting_time = models.CharField(max_length=50, verbose_name="Casting time",validators=[validate_is_profane])
    range = models.CharField(max_length=50,validators=[validate_is_profane])
    target = models.CharField(max_length=50, blank=False,validators=[validate_is_profane])
    components = models.CharField(max_length=50,validators=[validate_is_profane])
    duration = models.CharField(max_length=50,validators=[validate_is_profane])
    higher_levels = models.CharField(max_length=200, verbose_name="Higher level cast",validators=[validate_is_profane])
    spell_lists = models.CharField(max_length=100,verbose_name="Spell list",validators=[validate_is_profane])

    def get_absolute_url(self):
        return reverse("spell_detail", args=[str(self.id)])

    def __str__(self):
        return self.name
