# Generated by Django 2.1.8 on 2019-07-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ericaconvin', '0007_auto_20190723_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericaconvin.Category'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericaconvin.Category'),
        ),
    ]