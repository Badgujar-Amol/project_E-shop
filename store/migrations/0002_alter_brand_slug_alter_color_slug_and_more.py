# Generated by Django 4.0.1 on 2022-01-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='idealfor',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='necktype',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='occasion',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='sleeve',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
