# Generated by Django 4.2.9 on 2024-01-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0002_asset_assettype_assetimage_asset_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_code',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
