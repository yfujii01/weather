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
    tenki_text = '本日の天気は、' + tenki_element.text

    tenki_text = tenki_text.replace('雨', 'あめ')

    max_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.temp > span.value')
    max_text = '最高気温は、' + max_element.text + '度。'

    min_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.temp > span.value')
    min_text = '最低気温は、' + min_element.text + '度。'

    rain1_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(3)')
    rain1_text = '降水確率は、午前中が、' + rain1_element.text

    rain2_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(4)')
    rain2_text = '午後が、' + rain2_element.text

    if rain1_element.text == rain2_element.text:
        rain3_text = '降水確率は、' + rain1_element.text
    else:
        rain3_text = '降水確率は、午前中が、' + rain1_element.text + '、午後が、' + rain2_element.text

    # rain3_element = driver.find_element_by_css_selector(
    #     '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(5)')
    # rain3_text = '18時以降が、' + rain3_element.text

    max_dif_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.tempdiff')
    max_dif_ele = max_dif_element.text

    min_dif_element = driver.find_element_by_css_selector(
        '#main-column > section > div.forecast-days-wrap.clearfix > section.today-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.tempdiff')
    min_dif_ele = min_dif_element.text

    max_dif_ele = re.sub('[\[\]]', '', max_dif_ele)
    max_dif_ele_int = int(max_dif_ele)

    min_dif_ele = re.sub('[\[\]]', '', min_dif_ele)
    min_dif_ele_int = int(min_dif_ele)

    # dif_int = max_dif_ele_int + min_dif_ele_int
    # if dif_int > 0:
    #     dif_text = '昨日より' + str(dif_int) + '度ほど温かいでしょう'
    # else:
    #     dif_text = '昨日より' + str(dif_int) + '度ほど冷えるでしょう'

    if max_dif_ele_int > 0:
        dif_text = '昨日より' + str(max_dif_ele_int) + '度ほど温かいでしょう'
    elif max_dif_ele_int == 0:
        dif_text = '今日と同じくらいの暖かさでしょう'
    else:
        dif_text = '昨日より' + str(max_dif_ele_int) + '度ほど冷えるでしょう'

    talktext = 'ぴんぽん、本日の天気をお知らせします。'
    talktext += tenki_text + '。'
    talktext += rain3_text + '。'
    talktext += max_text + '。'
    talktext += min_text + '。'
    talktext += dif_text + '。'
    talktext += '以上、本日の天気予報でした'

    print(talktext)

    subprocess.call(['sh', 'jsay.sh', talktext])

except Exception:
    print('error')
    raise Exception

finally:
    driver.quit()
