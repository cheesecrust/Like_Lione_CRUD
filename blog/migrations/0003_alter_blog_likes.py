# Generated by Django 4.0.4 on 2022-04-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
