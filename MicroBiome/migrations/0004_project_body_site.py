# Generated by Django 2.2.2 on 2019-06-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MicroBiome', '0003_auto_20190611_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body_site',
            field=models.CharField(max_length=30, null=True),
        ),
    ]