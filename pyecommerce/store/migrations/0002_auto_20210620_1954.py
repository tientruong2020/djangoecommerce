# Generated by Django 3.1.7 on 2021-06-20 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderreport',
            old_name='created',
            new_name='createdAt',
        ),
    ]