from django.shortcuts import render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# Create your views here.
class JSONView(BaseLineChartView):
    def get_labels(self):
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name="index.html")
line_chart_json = JSONView.as_view()

# def index(request):
#     x_data = [0,1,2,3]
#     y_data = [x**2 for x in x_data]
#     plot_div = plot([scatter(x=x_data, y=y_data,
#                         mode='lines', name='test')],
#                         output_type='div')
#     return render(request, 'index.html', context={'plot_div': plot_div})