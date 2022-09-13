# Generated by Django 4.0.5 on 2022-09-13 15:30

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_dungeon_name_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dungeon_name',
            field=models.CharField(max_length=30, validators=[profanity.validators.validate_is_profane], verbose_name='Dungeon name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[profanity.validators.validate_is_profane], verbose_name='Username'),
        ),
    ]