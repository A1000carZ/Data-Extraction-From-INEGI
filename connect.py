import pymysql

server = 'hackaton.czla5cmf9lk9.us-east-1.rds.amazonaws.com'
database = 'hackaton'
username = 'admin'
password = 'a2d0m2i2n'

connection = pymysql.connect(host=server, database=database, user=username, password=password)

cursor = connection.cursor()

#sql = "DROP TABLE inegi;"
sql = "CREATE TABLE hackaton.inegi (srl_id serial NOT NULL,int_id_dataset BIGINT unsigned NULL,var_nombre character varying(250) NOT NULL,var_raz_social character varying(250) NOT NULL,var_actividad character varying(250) NOT NULL,var_total_empl character varying(100) NOT NULL,var_tipo_vialidad character varying(100) NOT NULL,var_vialidad character varying(300) NOT NULL,var_tipo_asent character varying(100) NOT NULL,var_asent character varying(250) NOT NULL,var_cp character varying(100) DEFAULT NULL,var_estado character varying(150) NOT NULL,var_municipio character varying(250) NOT NULL,var_localidad character varying(250) NOT NULL,CONSTRAINT inegi_pk PRIMARY KEY(srl_id));"

cursor.execute(sql)

cursor.close()