# Generated by Django 3.1.7 on 2021-04-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_payment_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=200, null=True),
        ),
    ]
