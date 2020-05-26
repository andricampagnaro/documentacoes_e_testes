from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox()
url='https://curso-python-selenium.netlify.app/aula_03.html'

navegador.get(url)

sleep(3)

# Pegar tag da ancora
a = navegador.find_element_by_tag_name('a')
p = navegador.find_element_by_tag_name('p')
print(f'a: {a.text}')
print(f'p: {p.text}')
a.click()

# navegador.quit()