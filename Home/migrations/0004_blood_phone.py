# Generated by Django 4.2.1 on 2023-10-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
