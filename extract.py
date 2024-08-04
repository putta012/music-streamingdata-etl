#!/usr/bin/env python
# coding: utf-8

# In[301]:


# import logging

# # Configure logging to output to a file
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("extract.log"),
#         # logging.StreamHandler()  # Optional: Keep this if you also want to see logs in the console
#     ]
# )
# logger = logging.getLogger(__name__)


import logging

# Create a logger specific to this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('extract.log')
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Ensure no handlers are duplicated
if logger.hasHandlers():
    logger.handlers.clear()
    logger.addHandler(file_handler)
# Prevent log messages from propagating to the root logger
logger.propagate = False

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)


# In[302]:


import mysql.connector
from mysql.connector import Error

def connectMysql(config):
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.info("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.info("Database does not exist")
        else:
            logger.error(err)

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logger.info(f"mysql>>     {query}")
        logger.info("Query executed successfully")
    except Error as e:
        logger.error(f"The error '{e}' occurred")
    else:
        cursor.close()


# In[303]:


import csv


def read_header(file_path):
    try:
        with open(file_path, mode='r', encoding='latin1') as file:
            csv_file = csv.reader(file)
            header = tuple(next(csv_file))
            return header
    except UnicodeDecodeError:
        logger.info("Error reading the file with 'latin1' encoding.")

def rawColumntypes_tuple(lengthVARCHAR,header_tuple):
    x = f"VARCHAR({lengthVARCHAR})"
    l = len(header_tuple)
    return (x,)*l

def prepare_DDLcreateTable(file_path, lengthVARCHAR):
    header = read_header(file_path)
    types = rawColumntypes_tuple(lengthVARCHAR, header)
    
    cols = ", ".join(tuple(map(lambda x,y : "`"+x+"`"+" "+y, header, types)))

    create_table = f"CREATE TABLE raw_data ({cols})"    
    return (create_table)



# x =pd.read_csv(file_path, encoding='latin')
# print(x.head(1))


# In[304]:


import pandas as pd

def createinsert(i, row, table):
    query = f"INSERT INTO {table} VALUES {row}"
    query = query.replace(", nan,", ",null,")
    logger.info(f"record number>>> {i} Insert Query>>>>>>>>>     {query}")    
    return query
    
def load_datatoMysql(file_path, cnx):
    try:
        df = pd.read_csv(file_path, encoding='Latin')
        # df.head(15)
        for i,row in df.iterrows():
            row_tup= tuple(row)
            logger.info(f"CSV ROW AS Tuple: {row_tup}")
            query = createinsert(i, row_tup, 'raw_data')
            
            execute_query(cnx, query)
            
            # print(query)
            # if(i==10):
            #     break
    except Exception as e:
        logger.error(f"{e}")



# In[305]:


##### MAIN ####

def readCSVloadtoDB():

    config = {'user': 'root', 
              #'password': '',
              'host': '127.0.0.1',
              #'database': '',
              'raise_on_warnings': True }
    file_path = '/Users/mamathaputta/Documents/selfGrowth/Acedemic/projects/py sql tableau/data/spotify-2023.csv' 
    # file_path = '/Users/mamathaputta/Documents/selfGrowth/Acedemic/projects/py sql tableau/data/spotify-2023.csv' 
    Q_create_db = "CREATE DATABASE music"
    Q_useDB = "USE music"
    Q_drop_db = "DROP DATABASE IF EXISTS music"
    Q_drop_table = "DROP TABLE IF EXISTS raw_data"
    Q_create_table = prepare_DDLcreateTable(file_path, 200)
    
    cnx = connectMysql(config)
    
    execute_query(cnx, Q_drop_db)
    execute_query(cnx, Q_create_db)
    execute_query(cnx, Q_useDB)
    # execute_query(cnx, Q_drop_table)
    execute_query(cnx, Q_create_table)
    load_datatoMysql(file_path, cnx)
    cnx.close()

readCSVloadtoDB()


# In[295]:


# import pandas as pd
# from sqlalchemy import create_engine, text


# username = 'root'
# password = ''
# host = '127.0.0.1'
# database = 'music'

# ## Load Data ##




# ## Retrive Data ##
# engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}")

# with engine.connect() as connection:
    
#     connection.execute(text(f"USE {database}"))
    
#     query = "select * from raw_data"
#     result_dataFrame = pd.read_sql(query,connection)
#     connection.close()

# result_dataFrame.head()


# In[262]:


# result_dataFrame.describe()
# result_dataFrame.info()


# In[263]:


# result_dataFrame.info()


# In[ ]:





# In[ ]:




