# Generated by Django 2.2.9 on 2020-02-26 13:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import teacherapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorTeachesModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(teacherapi.models.current_year), django.core.validators.MinValueValidator(1980)])),
                ('semester', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)])),
                ('module', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teacherapi.Module')),
                ('professor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teacherapi.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='UserRatesProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('module_instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacherapi.ProfessorTeachesModule')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='professors',
            field=models.ManyToManyField(through='teacherapi.ProfessorTeachesModule', to='teacherapi.Professor'),
        ),
    ]
