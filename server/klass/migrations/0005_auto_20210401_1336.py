# Generated by Django 3.1.7 on 2021-04-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klass', '0004_lc_main_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs',
            name='imgurl',
            field=models.TextField(default='Need to add'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lc',
            name='imgurl',
            field=models.TextField(default='Need to add'),
            preserve_default=False,
        ),
    ]