from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')
        submission = Submission.objects.create(enrollment=request.user)
        for choice_id in selected_choices:
            submission.choices.add(Choice.objects.get(pk=choice_id))
        return redirect('show_exam_result', course_id=course_id, submission_id=submission.id)
    return render(request, 'course_details_bootstrap.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'exam_result_bootstrap.html', {'submission': submission, 'course': course})
