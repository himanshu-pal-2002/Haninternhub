from django.db import models

class InternshipApplication(models.Model):

    title_of_internship = models.CharField(max_length=200)

    student_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=100, unique=True)

    course = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    year = models.IntegerField()
    semester = models.IntegerField()

    college = models.CharField(max_length=200)
    university_name = models.CharField(max_length=200)

    email = models.EmailField(unique=True)

    contact_number = models.CharField(max_length=10, unique=True)

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["registration_number", "title_of_internship"],
                name="unique_student_internship_application"
            )
        ]

    def __str__(self):
        return self.student_name