# Generated by Django 2.2.3 on 2019-10-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_cinfirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
