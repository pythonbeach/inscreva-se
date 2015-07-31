from django.shortcuts import render
from python_beach_boleto.core.forms import EnrollmentForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = EnrollmentForm()
    return render(request, 'index.html', {'form': form})
