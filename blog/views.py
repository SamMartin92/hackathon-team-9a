from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from django.contrib import messages
from .models import NGO, Event
from .forms import AddNGOForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


class AddNGOForm(CreateView):
    """ VIEW FOR ADD  """
    template_name = 'form.html'
    model = NGO
    form_class = AddNGOForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, 'Your NGO has been added successfully!')
        return redirect('index')
