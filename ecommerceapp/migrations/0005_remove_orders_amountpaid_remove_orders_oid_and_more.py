# Generated by Django 4.1.5 on 2023-04-14 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_prescribedproduct_prescribed_medicine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amountpaid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='paymentstatus',
        ),
    ]
