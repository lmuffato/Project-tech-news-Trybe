from datetime import datetime


format_date = '%Y-%m-%d'
format_datetime = '%Y-%m-%dT%H:%M:%S'


def validation_date(date):
    try:
        datetime.strptime(date, format_date)
    except ValueError:
        raise ValueError('Data inválida')
