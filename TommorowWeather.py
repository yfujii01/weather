from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess

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

    talktext = getTalkText(driver, css_tenki, css_max, css_min, css_rain1, css_rain2, css_maxdiff, css_mindiff, '今日',
                           '明日')

    print(talktext)

    subprocess.call(['sh', 'jsay.sh', talktext])


except Exception:
    print('error')
    raise Exception

finally:
    driver.quit()
