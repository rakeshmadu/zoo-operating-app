# Generated by Django 2.2.3 on 2019-08-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0004_auto_20190828_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Employ_id',
            field=models.PositiveIntegerField(default='0637'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='address',
            field=models.TextField(max_length=300),
        ),
    ]
