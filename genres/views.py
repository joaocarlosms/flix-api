from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def genres_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        genres = Genre(name=data['name'])
        genres.save()
        return JsonResponse(
            {'id': genres.id, 'name': genres.name}, 
            status=201
        )

@csrf_exempt
def genre_detail_view(request, pk):
    genres = get_object_or_404(Genre, pk=pk)
    data = {'id': genres.id, 'name': genres.name}
    return JsonResponse(data)