# Generated by Django 3.1.7 on 2021-04-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_payment_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
