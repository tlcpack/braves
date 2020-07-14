from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from sportsreference.mlb.roster import Roster, Player
from sportsreference.mlb.boxscore import Boxscore
from sportsreference.mlb.schedule import Schedule

from .models import Question, Player

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def player(request, pk):
#     player = get_object_or_404(Player, pk=pk)
#     return render(request, 'core/player.html', context={'player': player})

class DetailView(generic.DetailView):
    model = Question
    template_name = "core/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "core/results.html"

class PlayerView(generic.ListView):
    model = Player
    template_name = "core/players.html"

class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = "core/player.html"

def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'core/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('core:results', args=(question.id,)))

# class StatsPageView(TemplateView):
#     template_name = 'stats.html'

def stats(request):
    return render(request, 'stats.html')