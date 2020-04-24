import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# pegar url
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

# instanciar Firefox
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
# driver = webdriver.Firefox()

driver.get(url)
time.sleep(2)

xpath_botao = "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']"
driver.find_element_by_xpath(xpath_botao).click()

xpath_tabela = "//div[@class='nba-stat-table']//table"
element = driver.find_element_by_xpath(xpath_tabela)

html_content = element.get_attribute('outerHTML')

# parsear conteudo HTML
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# Estruturar conteudo em um dataframe
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)

# transformar os dados em um dicionário de dados prórpio
top10ranking = {}
top10ranking['points'] = df.to_dict('ranking')

print(top10ranking['points'])

driver.quit()

# converter e salvar em JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()