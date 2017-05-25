from django.db import models

class Url(models.Model):
    href = models.CharField(max_length=60)

class ServiceHistory(models.Model):
    Cartridge_Name = models.CharField(max_length=20)
    Used_by = models.CharField(max_length=60)
    In_Service = models.CharField(max_length=60)

class ProductionHistory(models.Model):
    Cartridge_Name = models.CharField(max_length=20)
    Designer = models.CharField(max_length=20)
    Designed = models.CharField(max_length=20)
    Manufacturer = models.CharField(max_length=30)
    Produced = models.CharField(max_length=20)
    Variants = models.CharField(max_length=20)

class Specs(models.Model):
    Cartridge_Name = models.CharField(max_length=20)
    Parent_case = models.CharField(max_length=20)
    Case_type = models.CharField(max_length=20)
    Bullet_diameter = models.CharField(max_length=20)
    Neck_diameter = models.CharField(max_length=10)
    Shoulder_diameter = models.CharField(max_length=10)
    Base_diameter = models.CharField(max_length=10)
    Rim_diameter = models.CharField(max_length=10)
    Rim_thickness = models.CharField(max_length=10)
    Case_length = models.CharField(max_length=20)
    Overall_length = models.CharField(max_length=20)
    Case_capacity = models.CharField(max_length=20)
    Rifling_twist = models.CharField(max_length=20)
    Primer_type = models.CharField(max_length=20)
    Maximum_pressure = models.CharField(max_length=20)

class BallisticPerformance(models.Model):
    Cartridge_Name = models.CharField(max_length=20)
    Bullet_mass_type = models.CharField(max_length=20)
    Velocity = models.CharField(max_length=20)
    Energy = models.CharField(max_length=20)
