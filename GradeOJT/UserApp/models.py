from statistics import mode
from django.db import models


class Sections(models.Model):
    SectionId = models.AutoField(primary_key=True)
    SectionYear = models.IntegerField()
    SectionName = models.CharField(max_length=100)

class Roles(models.Model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=100)

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    Role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    PhotoFileName = models.CharField(max_length=100)
    Section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    