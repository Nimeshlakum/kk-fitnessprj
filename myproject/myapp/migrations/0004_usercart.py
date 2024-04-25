# Generated by Django 5.0.4 on 2024-04-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.IntegerField(max_length=30)),
                ('product_quantity', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=10)),
                ('user_email', models.EmailField(max_length=30)),
            ],
            options={
                'db_table': 'usercart',
            },
        ),
    ]