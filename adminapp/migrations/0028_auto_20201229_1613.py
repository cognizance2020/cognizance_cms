# Generated by Django 3.1.4 on 2020-12-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0027_auto_20201229_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusupdates',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='statusupdates',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
