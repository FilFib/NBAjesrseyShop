# Generated by Django 4.2.7 on 2023-11-26 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_team_team_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderproducts",
            name="order_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.order"
            ),
        ),
        migrations.AlterField(
            model_name="orderproducts",
            name="product_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="shop.product"
            ),
        ),
        migrations.AlterField(
            model_name="orderproducts",
            name="product_variant_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="shop.productvariant"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="nba_player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="shop.nbaplayer"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="team_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="shop.team"
            ),
        ),
    ]
