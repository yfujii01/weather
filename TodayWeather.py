from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import re

options = Options()

options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

try:
    # Rakuten Infoseek 岡山市北区の天気
    driver.get('https://infoseek.tenki.jp/forecast/7/36/6610/33101/')
    tenki_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.weather-icon > p')
    tenki_text = '本日の天気は、' + tenki_element.text + ''

    max_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.temp > span.value')
    max_text = '最高気温は、' + max_element.text + '度'

    min_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.temp > span.value')
    min_text = '最低気温は、' + min_element.text + '度'

    rain1_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(3)')
    rain1_text = '降水確率は、お昼の12時までが、' + rain1_element.text

    rain2_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(4)')
    rain2_text = '12時から18時までが、' + rain2_element.text

    rain3_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(5)')
    rain3_text = '18時以降が、' + rain3_element.text

    max_dif_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.tempdiff')
    max_dif_ele = max_dif_element.text
    max_dif_ele = re.sub('[\[\]+-]', '', max_dif_ele)
    max_dif_ele_int = int(max_dif_ele)
    if int(max_dif_ele_int) > 0:
        max_dif_text = '前日より、' + max_dif_ele + '度高め'
    elif int(max_dif_ele_int) < 0:
        max_dif_text = '前日より、' + max_dif_ele + '度低め'
    else:
        max_dif_text = '前日と同じくらい'

    min_dif_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.tempdiff')
    min_dif_ele = min_dif_element.text
    min_dif_ele = re.sub('[\[\]+-]', '', min_dif_ele)
    min_dif_ele_int = int(min_dif_ele)
    if min_dif_ele_int > 0:
        min_dif_text = '前日より、' + min_dif_ele + '度高め'
    elif min_dif_ele_int < 0:
        min_dif_text = '前日より、' + min_dif_ele + '度低め'
    else:
        min_dif_text = '前日と同じくらい'

    print(tenki_text)
    print(rain1_text)
    print(rain2_text)
    print(rain3_text)
    print(max_text)
    print(max_dif_text)
    print(min_text)
    print(min_dif_text)

    subprocess.call(['sh', 'jsay.sh', 'ぴんぽん、本日の天気をお知らせします。'])
    subprocess.call(['sh', 'jsay.sh', tenki_text])
    subprocess.call(['sh', 'jsay.sh', rain1_text])
    subprocess.call(['sh', 'jsay.sh', rain2_text])
    subprocess.call(['sh', 'jsay.sh', rain3_text])
    subprocess.call(['sh', 'jsay.sh', max_text])
    subprocess.call(['sh', 'jsay.sh', max_dif_text])
    subprocess.call(['sh', 'jsay.sh', min_text])
    subprocess.call(['sh', 'jsay.sh', min_dif_text])
    subprocess.call(['sh', 'jsay.sh', 'です'])

except Exception:
    print('error')
    raise Exception

finally:
    driver.quit()
