# Generated by Django 2.2.7 on 2019-11-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_uyeler_cozulen_soru'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayarlar',
            name='cozulen_soru',
            field=models.IntegerField(default=0, verbose_name='Çözülen Soru'),
        ),
        migrations.AlterField(
            model_name='uyeler',
            name='cozulen_soru',
            field=models.IntegerField(default=0, verbose_name='Çözülen Soru'),
        ),
    ]