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
    selected_ids = submission.choices.values_list('id', flat=True)
    score = 0
    total = 0
    for question in course.question_set.all():
        total += 1
        if question.is_get_score(selected_ids):
            score += 1
    grade = (score / total) * 100 if total > 0 else 0
    context = {
        'course': course,
        'submission': submission,
        'selected_ids': selected_ids,
        'grade': grade,
    }
    return render(request, 'exam_result_bootstrap.html', context)
