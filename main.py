from rest_functions import extract_data, get_urls
from processing_functions import data_frame_process
import pymysql
import numpy as np

# You can specify the date of data
# from https://www.inegi.org.mx/app/descarga/ in "- Actividad economica" row
urls = get_urls('05/2022')

# You can specify the date of data
# from https://www.inegi.org.mx/app/descarga/ in "- Actividad economica" row
files = extract_data("05/2022")

frame = data_frame_process(files)

# This fix some empty field is the .csv files
frame['cod_postal'] = frame['cod_postal'].replace(np.nan, 0, regex=True)
# This convert double to int in postal code field
frame['cod_postal'] = frame['cod_postal'].astype(int)

# This fix some empty field is the .csv files
frame = frame.replace(np.nan, '', regex=True)

# Custom fields to extract
fr1 = frame[["nom_estab", "raz_social", "nombre_act", "per_ocu", 'tipo_vial', 'nom_vial', 'tipo_asent', 'nomb_asent',
             'cod_postal', 'entidad', 'municipio',
             'localidad']]

# This take only 1000000 of rows
data = fr1.head(1000000)

# ten.to_csv('file_name.csv', index=False)
# print(ten)

# You can configure your custom database
# Config sample
server = 'hackaton.czla5cmf9lk9.us-east-1.rds.amazonaws.com'
database = 'hackaton'
username = 'admin'
password = 'a2d0m2i2n'

# Getting ready a database
connection = pymysql.connect(host=server, database=database, user=username, password=password)

cursor = connection.cursor()

# This insert data to a database

# ------This is a sample-----------

# for i, row in fr1.iterrows():
#    data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],)
#    print(data)
#    # configure your table's name
#    sql = "INSERT INTO hackaton.inegi(var_nombre,var_raz_social,var_actividad,var_total_empl,var_tipo_vialidad,var_vialidad,var_tipo_asent,var_asent,var_cp,var_estado,var_municipio,var_localidad) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#    cursor.execute(sql, data)
#    connection.commit()

cursor.close()
# print(urls)

print(data)
