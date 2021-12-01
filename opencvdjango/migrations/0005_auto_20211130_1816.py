# Generated by Django 3.2.9 on 2021-11-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencvdjango', '0004_auto_20211130_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('doc', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='userentry',
            name='doc',
        ),
    ]