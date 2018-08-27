from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import re

from MyUtils import getTalkText

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

try:
    css_tenki = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.weather-icon > p'
    css_max = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.temp > span.value'
    css_min = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.temp > span.value'
    css_rain1 = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(3)'
    css_rain2 = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.precip-table > table > tbody > tr.rain-probability > td:nth-child(4)'
    css_maxdiff = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.high-temp.tempdiff'
    css_mindiff = '#main-column > section > div.forecast-days-wrap.clearfix > section.tomorrow-weather > div.weather-wrap.clearfix > div.date-value-wrap > dl > dd.low-temp.tempdiff'

    #
    #
    #
    # # Rakuten Infoseek 岡山市北区の天気
    # driver.get('https://infoseek.tenki.jp/forecast/7/36/6610/33101/')
    #
    # tenki_element = driver.find_element_by_css_selector(css_tenki)
    # tenki_text = '明日の天気は、' + tenki_element.text + ''
    #
    # max_element = driver.find_element_by_css_selector(css_max)
    # max_text = '最高気温は、' + max_element.text + '度'
    #
    # min_element = driver.find_element_by_css_selector(css_min)
    # min_text = '最低気温は、' + min_element.text + '度'
    #
    # rain1_element = driver.find_element_by_css_selector(css_rain1)
    # rain1_text = '降水確率は、午前中が、' + rain1_element.text
    #
    # rain2_element = driver.find_element_by_css_selector(css_rain2)
    # rain2_text = '午後が、' + rain2_element.text
    #
    # if rain1_element.text == rain2_element.text:
    #     rain3_text = '降水確率は、' + rain1_element.text
    # else:
    #     rain3_text = '降水確率は、午前中が、' + rain1_element.text + '、午後が、' + rain2_element.text
    #
    # max_dif_element = driver.find_element_by_css_selector(css_maxdiff)
    # max_dif_ele = max_dif_element.text
    #
    # min_dif_element = driver.find_element_by_css_selector(css_mindiff)
    # min_dif_ele = min_dif_element.text
    #
    # max_dif_ele = re.sub('[\[\]]', '', max_dif_ele)
    # max_dif_ele_int = int(max_dif_ele)
    #
    # min_dif_ele = re.sub('[\[\]]', '', min_dif_ele)
    # min_dif_ele_int = int(min_dif_ele)
    #
    # if max_dif_ele_int > 0:
    #     dif_text = '今日より' + str(max_dif_ele_int) + '度ほど温かいでしょう'
    # elif max_dif_ele_int == 0:
    #     dif_text = '今日と同じくらいの暖かさでしょう'
    # else:
    #     dif_text = '今日より' + str(max_dif_ele_int) + '度ほど冷えるでしょう'
    #
    # print(tenki_text)
    # # print(rain1_text)
    # # print(rain2_text)
    # print(rain3_text)
    # print(max_text)
    # print(min_text)
    # print(dif_text)
    #
    # subprocess.call(['sh', 'jsay.sh', 'ぴんぽん、明日の天気をお知らせします。'])
    # subprocess.call(['sh', 'jsay.sh', tenki_text])
    # # subprocess.call(['sh', 'jsay.sh', rain1_text])
    # # subprocess.call(['sh', 'jsay.sh', rain2_text])
    # subprocess.call(['sh', 'jsay.sh', rain3_text])
    # subprocess.call(['sh', 'jsay.sh', max_text])
    # subprocess.call(['sh', 'jsay.sh', min_text])
    # subprocess.call(['sh', 'jsay.sh', dif_text])
    # subprocess.call(['sh', 'jsay.sh', '以上、明日の天気予報でした'])

    talktext = getTalkText(driver, css_tenki, css_max, css_min, css_rain1, css_rain2, css_maxdiff, css_mindiff, '今日',
                           '明日')

    print(talktext)

    subprocess.call(['sh', 'jsay.sh', talktext])


except Exception:
    print('error')
    raise Exception

finally:
    driver.quit()
