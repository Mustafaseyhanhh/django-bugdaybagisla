# Generated by Django 2.2.7 on 2019-11-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ayarlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uyeler',
            name='engelle',
        ),
        migrations.AddField(
            model_name='uyeler',
            name='gsm',
            field=models.CharField(blank=True, max_length=50, verbose_name='Gsm'),
        ),
    ]
