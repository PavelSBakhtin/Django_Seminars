# Generated by Django 4.2.5 on 2023-10-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar3', '0002_post_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='showed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
