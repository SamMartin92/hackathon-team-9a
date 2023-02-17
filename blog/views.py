from django.shortcuts import render
from django.views.generic import ListView
from .models import NGO


# Create your views here.

def index(request):
    return render(request, 'index.html')


class NGOList(ListView):
    """
    List all NGOs
    """
    model = NGO
    template_name = 'listview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NGOList, self).get_context_data(*args, **kwargs)
        return context
