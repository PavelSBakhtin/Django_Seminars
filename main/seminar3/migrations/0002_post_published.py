# Generated by Django 4.2.5 on 2023-10-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
