# Generated by Django 5.0 on 2023-12-25 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='notices/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
            ],
        ),
    ]
