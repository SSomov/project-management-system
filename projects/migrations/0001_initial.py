# Generated by Django 2.0.3 on 2018-04-01 00:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(verbose_name='shortcut')),
                ('efforts', models.DurationField()),
                ('status',
                 models.CharField(choices=[('1', 'Stuck'), ('2', 'Working'),
                                           ('3', 'Done')],
                                  default=1,
                                  max_length=7)),
                ('dead_line', models.DateField()),
                ('complete_per',
                 models.FloatField(
                     max_length=2,
                     validators=[
                         django.core.validators.MinValueValidator(0),
                         django.core.validators.MaxValueValidator(100)
                     ])),
                ('description', models.TextField(blank=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('assign',
                 models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('task_name', models.CharField(max_length=80)),
                ('status',
                 models.CharField(choices=[('1', 'Stuck'), ('2', 'Working'),
                                           ('3', 'Done')],
                                  default=1,
                                  max_length=7)),
                ('due',
                 models.CharField(choices=[('1', 'On Due'), ('2', 'Overdue'),
                                           ('3', 'Done')],
                                  default=1,
                                  max_length=7)),
                ('assign',
                 models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.DO_NOTHING,
                     to='projects.Project')),
            ],
            options={
                'ordering': ['project', 'task_name'],
            },
        ),
    ]
