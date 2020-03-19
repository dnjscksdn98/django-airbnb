from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created'
    context_object_name = 'rooms'


class RoomDetail(DetailView):
    model = models.Room


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, 'rooms/detail.html', {'room': room})
#     except models.Room.DoesNotExist:
#         raise Http404()
