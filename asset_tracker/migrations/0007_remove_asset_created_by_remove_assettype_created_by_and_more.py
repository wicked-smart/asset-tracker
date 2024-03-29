# Generated by Django 4.2.9 on 2024-02-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0006_alter_asset_created_by_alter_assettype_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='assettype',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='asset',
            name='current_allocation_status',
            field=models.CharField(choices=[('ALLOCATED', 'Allocated'), ('UNALLOCATED', 'Unallocated')], default='UNALLOCATED', max_length=15),
        ),
    ]
