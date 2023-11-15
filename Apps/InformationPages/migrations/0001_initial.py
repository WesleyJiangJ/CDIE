# Generated by Django 4.1.6 on 2023-03-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmailClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('surname', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]