# Generated by Django 3.2.11 on 2022-02-04 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doneapp', '0004_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='country',
            new_name='district',
        ),
    ]
