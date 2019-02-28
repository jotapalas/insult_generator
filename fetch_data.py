from requests import get as get_request
from BeautifulSoup import BeautifulSoup

def get_insults():
  r = get_request('https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting')

  if r.status_code == 200:
    insults = []
    parsed_html = BeautifulSoup(r.text)
    table1 = parsed_html.body.find('table', attrs={
      'class' : 'article-table'
    })
    table2 = parsed_html.body.find('table', attrs={
      'class' : 'article-table article-table-selected'
    })
    table3 = parsed_html.body.findAll('table', attrs={
      'class' : 'article-table'
    })[1]

    insults.extend(get_insults_from_table(table1, 0, 1))
    insults.extend(get_insults_from_table(table2, 0, 1))
    insults.extend(get_insults_from_table(table3, 0, 2))
    insults.extend(get_insults_from_table(table3, 1, 2))
    return insults

def get_insults_from_table(table, insult_column, comeback_column):
  insults = []
  if table.find('th').text == 'Insult':
      for row in table.findAll('tr'):
        columns = row.findAll('td')
        if(len(columns) > 0):
          insults.append([columns[insult_column].text, columns[comeback_column].text])
  return insults