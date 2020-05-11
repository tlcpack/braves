from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'core/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/detail.html', {'question': question})

def results(request, q_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % q_id)

def vote(request, q_id):
    return HttpResponse("You're voting on question %s" % q_id)