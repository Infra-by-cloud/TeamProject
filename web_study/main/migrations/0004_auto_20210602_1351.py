# Generated by Django 3.2.3 on 2021-06-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='background',
            new_name='background1',
        ),
        migrations.AddField(
            model_name='home',
            name='background2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='home',
            name='background3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
