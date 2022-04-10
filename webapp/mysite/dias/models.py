from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    employee_count = models.IntegerField(default=100)
    domain = models.CharField(max_length=50)
    customer_serving = models.BooleanField(default=True)
    tech_company = models.BooleanField(default=True)
    accepts_user_input = models.BooleanField(default=False)
    is_listed = models.BooleanField(default=False)
    di_values = models.IntegerField(default=1)
    acs_values = models.IntegerField(default=1)
    di_resources = models.CharField(max_length=3000)
    acs_resources = models.CharField(max_length=3000)
    dias_score = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

class Complaint(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    complaint_type = models.CharField(max_length=20)
    complaint_proof = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
