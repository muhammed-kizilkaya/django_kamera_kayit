# Generated by Django 3.2.9 on 2021-11-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencvdjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='video_src',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]