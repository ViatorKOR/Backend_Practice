# Generated by Django 3.1.7 on 2021-04-16 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_data',
        ),
    ]