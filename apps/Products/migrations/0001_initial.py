# Generated by Django 4.1.1 on 2022-09-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('product_image', models.ImageField(blank=True, default='media/products/no_image.png', null=True, upload_to='media/products/')),
                ('status', models.PositiveSmallIntegerField(default=2)),
                ('length', models.FloatField(default=0.0)),
                ('width', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('weight', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, null=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('modified_date', models.DateField(auto_now=True, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
