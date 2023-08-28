# Generated by Django 4.2.4 on 2023-08-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, verbose_name='Token')),
                ('chat', models.CharField(max_length=200, verbose_name='Chat id')),
                ('message', models.TextField(verbose_name='Message text')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]