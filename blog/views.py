from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from django.contrib import messages
from .models import NGO, Event
from .forms import AddNGOForm


# Create your views here.


class Index(generic.ListView):
    def get(self, request):
        ngos = NGO.objects.all()[:8]
        feature_ngo = NGO.objects.all()[NGO.objects.count()-1]
        context = {
                "ngos": ngos,
                "feature_ngo": feature_ngo,
                }
        return render(request, 'index.html', context)


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


class NGOList(ListView):
    """
    List all NGOs
    """
    model = NGO
    template_name = 'listview.html'
    ngo_list = NGO.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(NGOList, self).get_context_data(*args, **kwargs)
        return context


class NGODetails(View):
    """
    NGO details
    """
    def get(self, request, *args, **kwargs):
        queryset = NGO.objects.all()
        ngo = get_object_or_404(queryset, pk=self.kwargs['pk'])

        return render(
            request,
            "detail.html",
            {
                "ngo": ngo,
            },
        )


def about(request):
    return render(request, 'about.html')


def setup(request):
    return render(request, 'setup.html')


def int_ngos(request):
    return render(request, 'int-ngos.html')
