# Generated by Django 4.0.3 on 2022-04-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220402_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='none', max_length=5000),
        ),
    ]
