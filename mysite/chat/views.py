from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# Create your views here.
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })