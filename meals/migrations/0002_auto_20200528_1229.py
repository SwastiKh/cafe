# Generated by Django 3.0.6 on 2020-05-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meal', 'verbose_name_plural': 'meals'},
        ),
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
