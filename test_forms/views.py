from django.shortcuts import render
from test_forms.forms import KidneyxForm

def index(request):
    form = KidneyxForm(initial={'vertexes':20, 'probability':0.1})
    return render(request, 'index.html', {'form': form})