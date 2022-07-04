# Generated by Django 4.0.4 on 2022-06-18 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(default='Company', max_length=50)),
                ('contactname', models.CharField(default='Contact', max_length=50)),
                ('phone', models.CharField(default='Phone', max_length=20)),
                ('address', models.CharField(default='Address', max_length=100)),
                ('postalcode', models.CharField(default='Postalcode', max_length=10)),
                ('city', models.CharField(default='City', max_length=50)),
                ('country', models.CharField(default='Country', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.DateField()),
                ('freight', models.CharField(default='Freight', max_length=10)),
                ('shipname', models.CharField(default='Ship name', max_length=50)),
                ('shipaddress', models.CharField(default='Shipping address', max_length=100)),
                ('shipcity', models.CharField(default='Shipcity', max_length=50)),
                ('country', models.CharField(default='Country', max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]