from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Exams,Question,Answer
# Create your views here.


class ExamListView(ListView):
    model = Exams
    template_name = "quiz/index.html"
    context_object_name = 'exams'


class ExamDetailView(DetailView):
    model = Exams
    template_name = "quiz/quiz.html"
    context_object_name = 'exams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self.object.question_set.all()
        return context


