# Generated by Django 2.2.1 on 2019-05-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_auto_20190512_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
