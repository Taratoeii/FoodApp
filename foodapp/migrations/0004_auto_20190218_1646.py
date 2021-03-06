# Generated by Django 2.1.4 on 2019-02-18 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_auto_20190216_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='pub_date',
            new_name='review_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='typefood',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='votes',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='typefood',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='foodapp.Typefood'),
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='typefood',
            name='typefood_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
