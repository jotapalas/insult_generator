from requests import get as get_request
from BeautifulSoup import BeautifulSoup

def get_insults():
  r = get_request('https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting')

  if r.status_code == 200:
    parsed_html = BeautifulSoup(r.text)
    html_tables = parsed_html.body.findAll('table', attrs={
      'class' : 'article-table'
    })

    insults = []
    for table in html_tables:
      if table.find('th').text == 'Insult':
        for row in table.findAll('tr'):
          columns = row.findAll('td')
          if(len(columns) > 0):
            insults.append([columns[0].text, columns[1].text])
    
    return insults
    