from django.shortcuts import render
from python_beach_boleto.core.forms import EnrollmentForm


def index(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EnrollmentForm()
    return render(request, 'index.html', {'form': form})
