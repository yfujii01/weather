from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess

options = Options()

options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

try:
    # Rakuten Infoseek 岡山市北区の天気
    driver.get('https://infoseek.tenki.jp/forecast/7/36/6610/33101/')
    tenki_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.weather-icon > p')
    tenki_text = '明日の天気は、' + tenki_element.text + ''

    max_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.temp > span.value')
    max_text = '最高気温は、' + max_element.text + '度'

    min_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.temp > span.value')
    min_text = '最低気温は、' + min_element.text + '度'

    print(tenki_text)
    print(max_text)
    print(min_text)

    subprocess.call(['sh', 'jsay.sh', 'ぴんぽん、明日の天気をお知らせします。'])
    subprocess.call(['sh', 'jsay.sh', tenki_text])
    subprocess.call(['sh', 'jsay.sh', max_text])
    subprocess.call(['sh', 'jsay.sh', min_text])
    subprocess.call(['sh', 'jsay.sh', 'です'])

except Exception:
    print('error')
    raise Exception

finally:
    driver.quit()
