# Generated by Django 3.1.14 on 2022-10-28 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skyapp', '0006_auto_20221027_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deparments', to='skyapp.department'),
        ),
    ]
