# Generated by Django 3.2 on 2021-05-01 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.TextField()),
                ('no_of_products', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField()),
                ('product_type', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='retail.brands')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField()),
                ('lname', models.TextField(default=' ')),
                ('address', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('products', models.ManyToManyField(to='retail.Products')),
            ],
            options={
                'ordering': ['fname'],
            },
        ),
    ]
