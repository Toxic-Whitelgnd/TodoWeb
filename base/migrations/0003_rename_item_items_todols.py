# Generated by Django 4.0.4 on 2022-04-30 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_items_text_alter_todolist_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item',
            new_name='todols',
        ),
    ]