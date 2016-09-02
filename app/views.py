from django.shortcuts import render

from .forms import HeightForm
from .models import Height


def height(request):

    f1 = HeightForm()
    if request.POST:
        f1 = HeightForm(request.POST)
        if f1.is_valid():
            cushion = f1.cleaned_data['cushion']
            faucet = f1.cleaned_data['faucet']
            Height.objects.create(cushion=cushion, faucet=faucet)
    objects = Height.objects.all().order_by('date_time')
    return render(request, 'height.html', {'f1': f1, 'height': objects})
