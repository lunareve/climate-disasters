import requests
from datetime import datetime

BASE_URI = 'https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?$filter={resource}'


def format_dates(from_date, to_date):
    """Formats dates into FEMA disaster api URL."""
    fd = from_date + 'T00:00:00.000z'
    td = to_date + 'T00:00:00.000z'
    return 'declarationDate ge \'{}\' and declarationDate le \'{}\''.format(fd, td)


def format_disasters(disasters):
    """Formats disaster types into FEMA disaster api URL."""
    filters = []
    for disaster in disasters:
        filters.append('incidentType eq ' + disaster)
    return 'and'.join(filters)


def format_all(from_date, to_date, disasters):
    """Puts dates and disasters together in the FEMA disaster api URL."""
    date_range = format_dates(from_date, to_date)

    if disasters:
        disaster_filter = format_disasters(disasters)
        full_filter = date_range + ' and ' + disaster_filter
    else:
        full_filter = date_range

    return BASE_URI.format(resource=full_filter)


def request(uri):
    """Returns disasters in JSON."""

    r = requests.get(uri)
    if r.status_code != 200:
        print('Status:', r.status_code, 'Problem with the request.')
    return r.json()
