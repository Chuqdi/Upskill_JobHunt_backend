from django.db import models



class Job(models.Model):
    isAdmin = models.BooleanField(default=False)
    isBusiness = models.BooleanField(default=False)


    company_name = models.TextField()
    company_location = models.TextField()
    nature_of_job = models.TextField()
    skills = models.TextField()
    academic_qualification = models.TextField()
    gender = models.TextField()
    age_bracket = models.TextField()
    years_of_experience = models.TextField()
    job_description = models.TextField()
    other_benefits = models.TextField()
    salary_range = models.TextField()
    application_deadline = models.DateField()

    def __str__(self) -> str:
        return self.id




