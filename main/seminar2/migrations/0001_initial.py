# Generated by Django 4.2.5 on 2023-10-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadsTails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_time', models.DateTimeField(max_length=50)),
                ('res', models.CharField(max_length=50)),
            ],
        ),
    ]
