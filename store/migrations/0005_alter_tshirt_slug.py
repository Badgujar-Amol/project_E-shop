# Generated by Django 4.0.1 on 2022-01-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_tshirt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, null=True, unique=True),
        ),
    ]