from django.shortcuts import render, redirect
from .models import Course, Submission

def submit(request, course_id):
    if request.method == 'POST':
        submission = Submission.objects.create(user=request.user, course_id=course_id)
        submission.save()
        return redirect('show_exam_result', course_id=course_id)

def show_exam_result(request, course_id):
    return render(request, 'exam_result.html')
