# Generated by Django 4.1.3 on 2023-02-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_category_typedesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='address',
            field=models.CharField(default='Nothing was provided', max_length=500),
            preserve_default=False,
        ),
    ]
