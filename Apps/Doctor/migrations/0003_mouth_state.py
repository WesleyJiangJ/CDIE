# Generated by Django 4.1.6 on 2023-06-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_mouth'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouth',
            name='state',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
