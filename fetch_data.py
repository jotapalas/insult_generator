from requests import get as get_request
from json import loads as to_json

def get_objects(obj):
  r = get_request('https://angular-vortex-230208.appspot.com/api/' + obj)

  if r.status_code == 200:
    response_json = to_json(r.text)
    return response_json[obj]

def get_insults():
  return get_objects('insults')

def get_comebacks():
  return get_objects('comebacks')