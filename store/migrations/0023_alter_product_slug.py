# Generated by Django 3.2.16 on 2023-01-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='detail_view', max_length=200),
        ),
    ]
