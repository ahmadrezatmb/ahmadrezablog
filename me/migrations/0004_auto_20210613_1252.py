# Generated by Django 3.2.4 on 2021-06-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_auto_20210613_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favmovie',
            name='firimage',
        ),
        migrations.RemoveField(
            model_name='favmovie',
            name='first',
        ),
        migrations.RemoveField(
            model_name='favmovie',
            name='sec',
        ),
        migrations.RemoveField(
            model_name='favmovie',
            name='secimage',
        ),
        migrations.RemoveField(
            model_name='favmovie',
            name='third',
        ),
        migrations.RemoveField(
            model_name='favmovie',
            name='thirdimage',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='firimage',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='first',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='sec',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='secimage',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='third',
        ),
        migrations.RemoveField(
            model_name='favmusic',
            name='thirdimage',
        ),
        migrations.AddField(
            model_name='favmovie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='favmovie',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='favmusic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='favmusic',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
