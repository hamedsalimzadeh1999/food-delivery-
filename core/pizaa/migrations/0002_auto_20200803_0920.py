# Generated by Django 3.0.8 on 2020-08-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizaa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='name',
            new_name='title',
        ),
    ]