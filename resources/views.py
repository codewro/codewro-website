from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views import generic


from taggit.models import Tag
from .models import Resource
from .forms import ResourceForm

def main_page(request):
    return render(request, 'index.html', {})

def code_of_conduct(request):
    return render(request, 'coc.html', {})

def resources_list(request):
    resources = Resource.objects.all()
    tags = Tag.objects.all().order_by('name')
    return render(request, 'resources_list.html', {'resources': resources, 'tags': tags})

def resource_detail(request):

    return render(request, 'resource_detail.html', {})

def tagIndexView(request, slug):
    resources = Resource.objects.filter(tags__slug=slug)
    tags = Tag.objects.all()
    return render(request, 'resources_list.html', {'resources': resources, 'tags': tags})

class CreateView(generic.CreateView):
    model = Resource
    template_name = 'resource_form.html'
    form_class = ResourceForm
    success_url = reverse_lazy('thanks')

def thanks(request):
    template_name = 'resource_thanks.html'
    return render(request, 'resource_thanks.html', {})
