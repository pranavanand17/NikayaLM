# Generated by Django 5.0.6 on 2025-02-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_borrowedbook_book_alter_borrowedbook_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(blank=True, default='profile_photos/default.jpg', null=True, upload_to='cover_photos/'),
        ),
    ]
