# Generated by Django 4.2.4 on 2023-09-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_category',
            new_name='adress',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='item_price',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='company',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='last_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='region',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
