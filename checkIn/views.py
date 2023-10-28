from django.shortcuts import render, get_object_or_404
from .models import Client, Employee, Note, Login

# Create your views here.


class CustomLoginView(Login):
    template_name = 'account/login.html'


def add_note(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        employee = request.user
        clock_in = request.POST.get('clock_in')
        clock_out = request.POST.get('clock_out')
        Note.objects.create(client=client, text=text, employee=employee,
                            clock_in=clock_in, clock_out=clock_out)
        # handle form submission and create and new note
    return render(request, 'add_note.html', {'client': client})


def client_notes(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    notes = Note.objects.filter(client=client).order_by('-timestamp')
    context = {'notes': notes}
    return render(request, 'client_notes.html', context)
