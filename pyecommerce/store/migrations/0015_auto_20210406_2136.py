# Generated by Django 3.1.7 on 2021-04-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='ispay',
            field=models.BooleanField(default=False),
        ),
    ]