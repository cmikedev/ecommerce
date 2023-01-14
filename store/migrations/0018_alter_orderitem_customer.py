# Generated by Django 3.2.16 on 2023-01-13 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20230113_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_name', to='store.order'),
        ),
    ]