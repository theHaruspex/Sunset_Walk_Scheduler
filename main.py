from astral.sun import sun
from astral.geocoder import database, lookup
from datetime import date, timedelta

from config import service


LA = lookup("Los Angeles", database())
LA_sun = sun(LA.observer, date=date.today(), tzinfo=LA.timezone)
LA_sunset_time = LA_sun['sunset']

walk_start_time = LA_sunset_time - timedelta(minutes=15)
walk_end_time = LA_sunset_time + timedelta(minutes=15)

datetime_strings = []
for datetime_object in (walk_start_time, walk_end_time):
    string = str(datetime_object).replace(' ', 'T')
    datetime_strings.append(string)


event = {
  'summary': 'Sunset Walk',
  'location': 'The predetermined route',
  'description': None,
  'start': {
    'dateTime': f'{datetime_strings[0]}',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': f'{datetime_strings[1]}',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [None],
  'attendees': [None],
  'reminders': {
    'useDefault': True
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))