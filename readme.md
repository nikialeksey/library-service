# Library service

A simple django web service for job interview purpose.

[![Mit License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/nikialeksey/meerk/library-service/master/LICENSE)
![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)

## DB scheme

|**Reader**|
|----|
|name|

|**Book**|
|-----|
|title|
|reader|

There is the migration generates 50k readers and 100k books. For simplicity reader ID starts 
from 1 to 50000 inclusive.

## API
- `/all/` - db export in `CSV` format
- `/reader/<reader_id>/` - reader info in `JSON` format

## Run
```bash
docker-compose up
```