# Generated by Django 5.0.4 on 2024-04-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_shiping'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField(max_length=30)),
                ('product_quantity', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=10)),
                ('user_email', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=100)),
                ('user_city', models.TextField(max_length=30)),
                ('user_state', models.TextField(max_length=30)),
                ('user_country', models.TextField(max_length=30)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]