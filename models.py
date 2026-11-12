from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.course.name}"

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    
    def is_get_score(self, selected_ids):
        correct_choices = list(self.choice_set.filter(is_correct=True).values_list('id', flat=True))
        selected = list(selected_ids)
        return set(correct_choices) == set(selected)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    def __str__(self):
        return f"Submission by {self.enrollment.user.username}"
