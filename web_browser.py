import xlsxwriter
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

import json


URL, request = 'http://python.org/downloads', ''

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page(java_script_enabled=False)
    try:
        page.set_default_timeout(10_000)
        page.goto(URL)
        request = page.content()
    except:
        pass
    finally:
        browser.close()


if request:
    soup = BeautifulSoup(request, 'lxml')

    release_version = soup.find_all('span', 'release-number')
    release_date = soup.find_all('span', 'release-date')
    download_link = soup.find_all('span', 'release-download')
    release_notes = soup.find_all('span', 'release-enhancements')

    python_versions_dict = {}

    # тут я по привычке перевожу всё в json чтоб можно было схранить и посмотреть всё ли верно сделал)
    # код в комментах позволит сохранить все те же данные, но в формате json

    # for i in range(1, len(release_version)):
    #     python_versions_dict[release_version[i].text] = {"release_date": release_date[i].text,
    #                                                      "download_link": 'https://python.org' + download_link[i].findNext('a')['href'],
    #                                                      "notes_link": release_notes[i].findNext('a')['href']}

    # with open('python_versions.json', 'w', encoding='utf-8') as file:
    #     json.dump(python_versions_dict, file, indent=4, ensure_ascii=False)

    # через генератор приводим каждый список в нормальный вид, получая в итоге нужные для записи данные
    release_version = [release_version[i].text for i in range(1, len(release_version))]
    release_date = [release_date[i].text for i in range(1, len(release_date))]
    download_link = ["https://python.org" + download_link[i].findNext('a')['href'] for i in range(1, len(download_link))]
    release_notes = [release_notes[i].findNext('a')['href'] for i in range(1, (len(release_notes)))]

    all_data_list = [release_version, release_date, download_link, release_notes]

    col_name = [["A", 'version'], ["B", 'release date'], ["C", 'download link'], ["D", 'notes link']]
    work_book = xlsxwriter.Workbook("python_versions.xlsx")
    work_sheet = work_book.add_worksheet()

    for index in range(len(col_name)):
        work_sheet.write(f"{col_name[index][0]}1", col_name[index][1])

    for i in range(1, len(release_version)):
        for j in range(len(col_name)):
            work_sheet.write(f"{col_name[j][0]}{i + 1}", all_data_list[j][i])

    work_book.close()

    print("Данные успешно загружены и сохранены!)")

else:
    print('В процессе загрузки произошла ошибка. Проверьте url и повторите запрос')
