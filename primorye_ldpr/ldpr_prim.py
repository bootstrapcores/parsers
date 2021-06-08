from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Chrome()


def get_links(url, pdown):
    links_list = []

    driver.get(url)
    time.sleep(3)
    html = driver.find_element(By.TAG_NAME, "html")
    for i in range(pdown):
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    elems = driver.find_element(By.CSS_SELECTOR, 'div.layout.event-layout.column'). \
        find_elements(By.CSS_SELECTOR, 'a.event.v-card.v-sheet.theme--light.elevation-0')

    for elem in elems:
        href = elem.get_attribute('href')
        links_list.append(href)
    time.sleep(3)

    return links_list


def get_info(url):
    driver.get(url)
    time.sleep(3)
    elem_title = driver.find_element(By.CSS_SELECTOR, 'div.e-title.text-center.small')
    title_cur = elem_title.text

    elem_content = driver.find_element(By.CSS_SELECTOR, 'div.flex.subheading.font-weight-light.pa-3.event-content')
    content_cur = elem_content.text

    return title_cur, content_cur


main_url = 'https://primorye.ldpr.ru'
pdown_num = 20
links = get_links(main_url, pdown_num)

pars_dict = {}

n = 0
for link in links:
    n += 1
    title, content = get_info(link)

    pars_dict[n] = {}
    pars_dict[n]['link'] = link
    pars_dict[n]['title'] = title
    pars_dict[n]['content'] = content

print(pars_dict)

with open('ldpr.json', 'w', encoding='utf8') as fp:
    json.dump(pars_dict, fp, ensure_ascii=False)

driver.close()
driver.quit()
