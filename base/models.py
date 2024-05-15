from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('CM', 'Constituency Member'),
        ('GO', 'Government Official'),
    )
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

class Project(models.Model):
    STATUS_CHOICES = (
        ('P', 'Proposed'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    comments = models.ManyToManyField('Comment', blank=True)
    progress_updates = models.ManyToManyField('ProgressUpdate', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.date}'

class ProgressUpdate(models.Model):
    update_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Update by {self.author} on {self.date}'

class BursaryApplication(models.Model):
    INSTITUTION_LEVEL_CHOICES = (
        ('C', 'College'),
        ('HS', 'High School'),
    )
    applicant_name = models.CharField(max_length=200)
    contact_information = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    institution_level = models.CharField(max_length=2, choices=INSTITUTION_LEVEL_CHOICES)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f'Application by {self.applicant_name}'

class GovernmentFeedback(models.Model):
    feedback_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Feedback by {self.author} on {self.date}'

class Analytics(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    number_of_comments = models.IntegerField(default=0)
    number_of_progress_updates = models.IntegerField(default=0)
    bursary_applications_statistics = models.JSONField(default=dict)
    feedback_from_government = models.JSONField(default=dict)

    def __str__(self):
        return f'Analytics for project {self.project.title}'
