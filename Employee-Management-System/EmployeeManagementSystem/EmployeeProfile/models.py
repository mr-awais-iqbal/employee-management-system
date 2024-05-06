from django.db import models
class Designation (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self) -> str:
        return self.title
    
class JobDescription(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name
    
class Location (models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    def __str__(self) -> str:
        return self.name

    
class Department (models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=200)
    fatherName = models.CharField(max_length=200)
    dateOfJoining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designition = models.ForeignKey(Designation , on_delete=models.CASCADE)
    jobDescription = models.ForeignKey(JobDescription , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name