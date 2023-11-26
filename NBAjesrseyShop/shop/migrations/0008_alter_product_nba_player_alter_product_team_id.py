# Generated by Django 4.2.7 on 2023-11-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_address_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nba_player',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.nbaplayer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='team_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.team'),
        ),
    ]
