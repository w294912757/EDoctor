# Generated by Django 3.1.7 on 2021-03-15 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210315_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='userId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='backend.user'),
        ),
    ]
