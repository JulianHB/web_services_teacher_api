# Generated by Django 2.2.9 on 2020-02-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
