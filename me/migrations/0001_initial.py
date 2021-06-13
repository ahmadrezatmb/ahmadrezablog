# Generated by Django 3.2.4 on 2021-06-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favmovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=200)),
                ('firimage', models.CharField(max_length=200)),
                ('sec', models.CharField(max_length=200)),
                ('secimage', models.CharField(max_length=200)),
                ('third', models.CharField(max_length=200)),
                ('thirdimage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='favmusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=200)),
                ('firimage', models.CharField(max_length=200)),
                ('sec', models.CharField(max_length=200)),
                ('secimage', models.CharField(max_length=200)),
                ('third', models.CharField(max_length=200)),
                ('thirdimage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htmlcss', models.IntegerField()),
                ('boots', models.IntegerField()),
                ('python', models.IntegerField()),
                ('cpp', models.IntegerField()),
                ('js', models.IntegerField()),
                ('django', models.IntegerField()),
                ('godot', models.IntegerField()),
                ('php', models.IntegerField()),
                ('wp', models.IntegerField()),
            ],
        ),
    ]
