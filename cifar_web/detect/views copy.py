from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.
# rooms = [
#     {'id': 1, 'name':'tanatan', 'age':19},
#     {'id': 2, 'name':'tanatan2', 'age':12},
#     {'id': 3, 'name':'tanatan3', 'age':15},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, "tutorial/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk,)
    # for i in room:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}
    return render(request, "tutorial/room.html", context)

def create_rooms(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, "tutorial/room_form.html", context)

def update_rooms(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    context = {'form':form}
    return render(request, 'tutorial/room_form.html', context)