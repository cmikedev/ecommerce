# Generated by Django 3.2.16 on 2023-01-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_orderitem_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='add_slug', max_length=200),
        ),
    ]