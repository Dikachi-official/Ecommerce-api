# Generated by Django 4.1.2 on 2022-10-18 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0005_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
    ]