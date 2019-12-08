import csv
import json

from django.db.models.base import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponseNotFound

from .models import Book
from .models import Reader


def all(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="db_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['book_title', 'reader_name'])
    for book in Book.objects.all():
        writer.writerow([book.title, book.reader.name])

    return response


def reader_info(request, reader_id):
    try:
        reader = Reader.objects.get(pk=reader_id)
        books = list(map(lambda book: {"id": book.id, "title": book.title}, list(Book.objects.filter(reader=reader))))
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
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Reader by id {reader_id} was not found')