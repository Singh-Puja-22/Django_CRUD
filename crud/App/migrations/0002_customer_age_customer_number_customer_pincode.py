# Generated by Django 5.0.4 on 2024-04-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]