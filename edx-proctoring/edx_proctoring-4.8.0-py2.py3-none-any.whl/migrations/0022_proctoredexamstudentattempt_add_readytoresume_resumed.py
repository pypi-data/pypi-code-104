# Generated by Django 3.2.7 on 2021-10-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_proctoring', '0021_auto_20211029_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproctoredexamstudentattempt',
            name='ready_to_resume',
            field=models.BooleanField(default=False, verbose_name='Ready to Resume'),
        ),
        migrations.AddField(
            model_name='historicalproctoredexamstudentattempt',
            name='resumed',
            field=models.BooleanField(default=False, verbose_name='Resumed'),
        ),
        migrations.AddField(
            model_name='proctoredexamstudentattempt',
            name='ready_to_resume',
            field=models.BooleanField(default=False, verbose_name='Ready to Resume'),
        ),
        migrations.AddField(
            model_name='proctoredexamstudentattempt',
            name='resumed',
            field=models.BooleanField(default=False, verbose_name='Resumed'),
        ),
    ]
