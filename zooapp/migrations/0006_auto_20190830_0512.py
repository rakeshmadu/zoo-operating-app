# Generated by Django 2.2.3 on 2019-08-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0005_auto_20190829_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='Employ_id',
            field=models.PositiveIntegerField(default='2529'),
        ),
    ]
