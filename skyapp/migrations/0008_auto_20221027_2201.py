# Generated by Django 3.1.14 on 2022-10-28 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skyapp', '0007_auto_20221027_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='departments',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='dep', to='skyapp.Department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='chief_employee',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='skyapp.employee'),
        ),
    ]
