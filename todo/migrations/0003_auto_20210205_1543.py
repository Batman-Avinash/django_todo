# Generated by Django 3.1.6 on 2021-02-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210205_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Complete', 'complete'), ('Remaining', 'remaining')], default='Remaining', max_length=10),
        ),
    ]
