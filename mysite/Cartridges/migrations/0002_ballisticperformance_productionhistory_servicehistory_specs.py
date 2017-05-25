# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartridges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BallisticPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cartridge_Name', models.CharField(max_length=20)),
                ('Bullet_mass_type', models.CharField(max_length=20)),
                ('Velocity', models.CharField(max_length=20)),
                ('Energy', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cartridge_Name', models.CharField(max_length=20)),
                ('Designer', models.CharField(max_length=20)),
                ('Designed', models.CharField(max_length=20)),
                ('Manufacturer', models.CharField(max_length=30)),
                ('Produced', models.CharField(max_length=20)),
                ('Variants', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cartridge_Name', models.CharField(max_length=20)),
                ('Used_by', models.CharField(max_length=60)),
                ('In_Service', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cartridge_Name', models.CharField(max_length=20)),
                ('Parent_case', models.CharField(max_length=20)),
                ('Case_type', models.CharField(max_length=20)),
                ('Bullet_diameter', models.CharField(max_length=20)),
                ('Neck_diameter', models.CharField(max_length=10)),
                ('Shoulder_diameter', models.CharField(max_length=10)),
                ('Base_diameter', models.CharField(max_length=10)),
                ('Rim_diameter', models.CharField(max_length=10)),
                ('Rim_thickness', models.CharField(max_length=10)),
                ('Case_length', models.CharField(max_length=20)),
                ('Overall_length', models.CharField(max_length=20)),
                ('Case_capacity', models.CharField(max_length=20)),
                ('Rifling_twist', models.CharField(max_length=20)),
                ('Primer_type', models.CharField(max_length=20)),
                ('Maximum_pressure', models.CharField(max_length=20)),
            ],
        ),
    ]