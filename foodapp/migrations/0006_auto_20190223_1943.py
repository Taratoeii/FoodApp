# Generated by Django 2.1.4 on 2019-02-23 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_review_name_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaurant',
            new_name='review_res',
        ),
    ]
