# Generated by Django 3.1.2 on 2020-11-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201102_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='reference',
        ),
        migrations.AlterField(
            model_name='ride',
            name='payment_method',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Card')], default=2),
        ),
    ]
