# Generated by Django 3.2.6 on 2022-05-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apinews', '0006_auto_20220529_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]