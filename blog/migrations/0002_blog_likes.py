# Generated by Django 4.0.4 on 2022-04-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
