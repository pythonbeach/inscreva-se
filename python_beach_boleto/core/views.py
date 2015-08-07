from django.shortcuts import render

from python_beach_boleto.core.forms import EnrollmentForm, RecoveryPayment
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


def recovery_by_email(request):
    if request.method == 'POST':
        form = RecoveryPayment(request.POST)
        email = form.data['email']
        enroll = Enrollment.objects.get(email=email)
        return payment(request, enroll.id)
    else:
        form = RecoveryPayment()
    return render(request, 'recovery_by_email.html', {'form': form})
