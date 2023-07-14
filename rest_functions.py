from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import io
import zipfile
import os


def get_urls(date):
    opts = Options()

    opts.add_argument("headless")

    url = "https://www.inegi.org.mx/app/descarga/"

    driver = webdriver.Chrome(options=opts)

    urls = []

    try:
        driver.get(url)

        page_source = driver.page_source

        bs = BeautifulSoup(page_source, 'html.parser')

        table = bs.find(id='tblDescargaArchivos_denue').find('tbody').find_all('tr', {
            'data-titulopadre': 'Otros|DENUE|Actividad económica'})

        for item in table:
            date_td = item.findNext('td', {'style': 'padding:5px !important;'})
            title = item.get('data-titulo')
            if date_td.text == date and title != "Otros|DENUE|Actividad económica|Actividades legislativas, gubernamentales, de impartición de justicia y de organismos internacionales y extraterritoriales":
                url_item = item.find_all_next('a')[1].get('href')
                urls.append('https://www.inegi.org.mx' + url_item)

    except Exception:
        print('Error: Something went wrong :(')

    driver.quit()

    return urls


def get_files(urls):
    list_csv = []
    try:
        print("Founded", len(urls), "files")
        for i, url in enumerate(urls, start=0):
            file_zip = requests.get(url)
            zip_file = zipfile.ZipFile(io.BytesIO(file_zip.content))

            for member in zip_file.namelist():
                if member.startswith('conjunto') and member.endswith('csv'):
                    percentage = (i * 100) / len(urls)
                    rounded_percentage = round(percentage,2)
                    file = zip_file.extract(member)
                    list_csv.append(file)
                    print("Downloading...", rounded_percentage, "%")
        print("Downloaded!")
    except Exception:

        print('Error getting files :(')

    return list_csv


def extract_data(date):
    files = []

    directory = 'conjunto_de_datos'

    exist_directory = os.path.exists(directory)

    print("Searching files...")

    if exist_directory:
        for dirpath, _, filenames in os.walk(directory):
            for f in filenames:
                files.append(os.path.abspath(os.path.join(dirpath, f)))
    else:
        urls = get_urls(date=date)
        print('Generating download...')
        files = get_files(urls)

    return files
