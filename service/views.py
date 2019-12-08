import csv
import json

from django.db.models.base import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404

from .models import Book
from .models import Reader


def all(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="db_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['book_title', 'reader_name'])
    for book in Book.objects.all():
        reader = book.reader
        reader_name = ""
        if reader:
            reader_name = reader.name
        writer.writerow([book.title, reader_name])

    return response


def reader_info(request, reader_id):
    reader = get_object_or_404(Reader, pk=reader_id)
    books = list(
        map(
            lambda book: {"id": book.id, "title": book.title},
            list(Book.objects.filter(reader=reader))
        )
    )
    return HttpResponse(
        json.dumps(
            {
                'reader': {
                    'id': reader.id,
                    'name': reader.name,
                },
                'books': books,
            }
        ),
        content_type='application/json'
    )


def reader_id_bounds(request):
    return HttpResponse(
        f'From {Reader.objects.first().id} to {Reader.objects.last().id}'
    )
