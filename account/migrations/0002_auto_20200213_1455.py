# Generated by Django 2.2.8 on 2020-02-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='scientist',
            field=models.NullBooleanField(default=False),
        ),
    ]
