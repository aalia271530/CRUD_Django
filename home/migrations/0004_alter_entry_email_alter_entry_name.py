# Generated by Django 5.0.1 on 2024-02-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_entry_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='EMAIL',
            field=models.CharField(max_length=51, unique=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='NAME',
            field=models.CharField(max_length=51),
        ),
    ]
