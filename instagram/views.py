from django.shortcuts import render
from .models import port
# Create your views here.


def port_list(request):
    qs = port.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    #instagram/templates/instagram/port_list.html
    return render(request, 'instagram/port_list.html', {
        'port_list': qs,
        'q': q,
    })