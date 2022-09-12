# Generated by Django 4.1.1 on 2022-09-12 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargesPerWarehouse',
            fields=[
                ('charges_per_warehouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('prep_charges', models.FloatField(default=0.0)),
                ('pickup_charges', models.FloatField(default=0.0)),
                ('shipping_charges', models.FloatField(default=0.0)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('modified_date', models.DateField(auto_now=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='charges_per_warehouse_product_fk', to='Products.product')),
                ('warehouse_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='charges_per_warehouse_warehouse_fk', to='Products.warehouse')),
            ],
            options={
                'db_table': 'charges_per_warehouse',
            },
        ),
    ]