# Generated by Django 2.1.4 on 2019-02-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20190218_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
