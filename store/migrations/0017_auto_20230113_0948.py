# Generated by Django 3.2.16 on 2023-01-13 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20230113_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_table', to='store.order'),
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
