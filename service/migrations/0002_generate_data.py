import random

from django.db import migrations


def generate_data(apps, schema_editor):
    Book = apps.get_model('service', 'Book')
    Reader = apps.get_model('service', 'Reader')

    readers = []
    for i in range(50_000):
        reader = Reader(name=f"Reader {i}")
        reader.save()
        readers.append(reader)

    for i in range(100_000):
        Book(title=f"Book {i}", reader=readers[random.randint(0, len(readers) - 1)]).save()


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0001_initial')
    ]

    operations = [
        migrations.RunPython(generate_data, reverse_code=migrations.RunPython.noop),
    ]
