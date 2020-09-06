from selenium import webdriver
import datetime
import os

f = open('products.txt', 'r')
products = f.readlines()

output = open('output.csv', 'a')

driver = webdriver.Chrome('./chromedriver')

try:
    header = ['']
    data = [str(datetime.datetime.now())]
    for url in products:
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_class_name('heading')
        elem = elem.find_element_by_tag_name('h2')
        name = elem.text

        elem = driver.find_element_by_class_name('prdc_default_info')
        elem = elem.find_element_by_class_name('sale_price')
        price = elem.text

        header.append(name.replace(',', ''))
        data.append(price.replace(',', ''))

    if not os.path.exists('output.csv'):
        output.write(','.join(header)+'\n')

    output.write(','.join(data)+'\n')

except Exception as e:
    print(e)
finally:
    driver.quit()
