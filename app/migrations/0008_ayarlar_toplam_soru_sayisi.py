# Generated by Django 2.2.7 on 2019-11-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191126_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='toplam_soru_sayisi',
            field=models.IntegerField(default=0, verbose_name='Toplam Soru Sayisi'),
        ),
    ]
