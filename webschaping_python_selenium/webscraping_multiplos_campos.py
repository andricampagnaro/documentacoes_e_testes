import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# pegar url
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

# criar a estrutura de rankings
top10ranking = {}

rankings = {'3points': {'field': 'FG3M', 'label': '3PM'},
            'points': {'field': 'PTS', 'label': 'PTS'},
            'assistants': {'field': 'AST', 'label': 'AST'},
            'rebounds': {'field': 'REB', 'label': 'REB'},
            'steals': {'field': 'STL', 'label': 'STL'},
            'blocks': {'field': 'BLK', 'label': 'BLK'}}

def buildrank(type):
    field = rankings[type]['field']
    label = rankings[type]['label']


    xpath_botao = f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']"
    driver.find_element_by_xpath(xpath_botao).click()

    xpath_tabela = "//div[@class='nba-stat-table']//table"
    element = driver.find_element_by_xpath(xpath_tabela)

    html_content = element.get_attribute('outerHTML')

    # parsear conteudo HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')

    # Estruturar conteudo em um dataframe
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']

    # transformar os dados em um dicionário de dados prórpio
    return df.to_dict('records')

# instanciar Firefox
option = Options()
option.headless = True
# driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()

driver.get(url)
time.sleep(2)

for k in rankings:
    top10ranking[k] = buildrank(k)

driver.quit()

# converter e salvar em JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()