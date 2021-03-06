from app import app

@app.template_filter()
def price(price):
    return '{:,}'.format(price).replace(',', ' ')

@app.template_filter()
def clear_direction(direction):
  return direction.replace('Из', '')

@app.template_filter()
def destination_url(destination):
  return f'/from/{destination}/'