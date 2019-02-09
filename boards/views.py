from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Board
from django.http import Http404

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    #for board in boards:
        #boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)

    return render(request, 'home.html', { 'boards': boards}) #HttpResponse(response_html)

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})