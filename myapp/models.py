from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# models.py


class HireMe(models.Model):
    company_name = models.CharField(max_length=255)
    salary_offering = models.DecimalField(max_digits=10, decimal_places=2)
    bond = models.BooleanField(default=False)
    bond_duration_years = models.PositiveIntegerField(null=True, blank=True)
    your_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    email_id = models.EmailField()

    def __str__(self):
        return f"{self.company_name} - {self.your_name}"




class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
