# Generated by Django 4.2.6 on 2023-10-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_toy', models.CharField(max_length=20)),
                ('price_toy', models.IntegerField()),
            ],
        ),
    ]
