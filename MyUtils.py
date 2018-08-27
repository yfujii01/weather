import re


def getTalkText(driver, css_tenki, css_max, css_min, css_rain1, css_rain2, css_maxdiff, css_mindiff, yesterday, today):
    global talktext
    # Rakuten Infoseek 岡山市北区の天気
    driver.get('https://infoseek.tenki.jp/forecast/7/36/6610/33101/')

    tenki_element = driver.find_element_by_css_selector(css_tenki)
    tenki_text = tenki_element.text
    tenki_text = tenki_text.replace('雨', 'あめ')

    max_element = driver.find_element_by_css_selector(css_max)
    max_text = '最高気温は、' + max_element.text + '度'
    min_element = driver.find_element_by_css_selector(css_min)
    min_text = '最低気温は、' + min_element.text + '度'

    rain1_element = driver.find_element_by_css_selector(css_rain1)
    rain1_text = '降水確率は、午前中が、' + rain1_element.text

    rain2_element = driver.find_element_by_css_selector(css_rain2)
    rain2_text = '午後が、' + rain2_element.text

    if rain1_element.text == rain2_element.text:
        rain3_text = '降水確率は、' + rain1_element.text
    else:
        rain3_text = '降水確率は、午前中が、' + rain1_element.text + '、午後が、' + rain2_element.text

    max_dif_element = driver.find_element_by_css_selector(css_maxdiff)
    max_dif_ele = max_dif_element.text
    min_dif_element = driver.find_element_by_css_selector(css_mindiff)
    min_dif_ele = min_dif_element.text
    max_dif_ele = re.sub('[\[\]]', '', max_dif_ele)
    max_dif_ele_int = int(max_dif_ele)
    min_dif_ele = re.sub('[\[\]]', '', min_dif_ele)
    min_dif_ele_int = int(min_dif_ele)
    if max_dif_ele_int > 0:
        dif_text = yesterday + 'より' + str(max_dif_ele_int) + '度ほど暑さでしょう'
    elif max_dif_ele_int == 0:
        dif_text = yesterday + 'と同じくらい暑くなるでしょう'
    else:
        dif_text = yesterday + 'より' + str(max_dif_ele_int) + '度ほど冷えるでしょう'

    talktext = 'ぴんぽん、' + today + 'の天気をお知らせします。'
    talktext += today + 'の天気は、' + tenki_text + '。'
    talktext += rain3_text + '。'
    talktext += max_text + '。'
    talktext += min_text + '。'
    talktext += dif_text + '。'
    talktext += '以上、' + today + 'の天気予報でした'

    return talktext
