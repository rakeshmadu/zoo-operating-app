# Generated by Django 2.2.3 on 2019-09-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooapp', '0010_auto_20190904_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Ticket_id',
            field=models.PositiveIntegerField(default='2969'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Employ_id',
            field=models.PositiveIntegerField(default='4843'),
        ),
    ]
