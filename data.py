import mock_data as mock_data

def get_tours(direction=None):
  tours = map(lambda key: {'id': key, **mock_data.tours[key] } ,mock_data.tours.keys())

  if not direction:
    return tours

  return list(filter(lambda tour: tour['departure'] == direction, tours))


def get_direction_info(direction):
    pass


def get_tour(tour_id):
  tour = mock_data.tours[int(tour_id)]

  if tour:
    return {
      'id': tour_id,
      **tour  
    }


def get_menu_departures():
    return mock_data.departures
