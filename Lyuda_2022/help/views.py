from django.shortcuts import render, HttpResponseRedirect
from .models import Question
from .forms import QuestionForm


def help_index(request):
    form = QuestionForm
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body']
            )
            question.save()
            return HttpResponseRedirect('/help/')
    questions = Question.objects.all().order_by('-created_on')
    context = {
        'questions': questions,
        'form': form
    }
    return render(request, 'help_index.html', context)