# Generated by Django 3.2.13 on 2022-07-24 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_userinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='foodid',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='orderid',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
