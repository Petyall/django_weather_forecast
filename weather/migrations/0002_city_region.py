# Generated by Django 5.0.7 on 2024-07-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
