# Generated by Django 3.2.11 on 2022-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doneapp', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=100)),
            ],
        ),
    ]
