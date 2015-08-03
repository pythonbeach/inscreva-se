from django.shortcuts import render

from python_beach_boleto.core.forms import EnrollmentForm
from python_beach_boleto.core.models import Enrollment


def payment(request, id_enroll):
    enroll = Enrollment.objects.get(pk=id_enroll)
    context = {'enroll': enroll}
    return render(request, 'payment.html', context)


def index(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enroll = form.save()
            return payment(request, enroll.id)
    else:
        form = EnrollmentForm()
    return render(request, 'index.html', {'form': form})
