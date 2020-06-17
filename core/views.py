from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from sportsreference.mlb.roster import Roster, Player
from sportsreference.mlb.boxscore import Boxscore
from sportsreference.mlb.schedule import Schedule

from .models import Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "core/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "core/results.html"


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
    all_scored = []
    all_allowed = []
    game_numbers = []
    atl_schedule = Schedule('ATL', '1995')
    runs = [game.runs_scored for game in atl_schedule]
    braves = Roster('ATL', '1995')
    pitchers = [player for player in braves.players if player.position == 'P']

    context = {
        'pitchers': pitchers,
    }
    return render(request, 'stats.html', context=context)