import re
import sys
import datetime as dt
import pandas as pd
import numpy as np
import  pymysql
from sqlalchemy import create_engine


def upload_data(df,name,method="append"):
    """
    输入DataFrame,name,append/replace
    """
    df= df
    name = name
    method = method
    engine = create_engine('mysql+pymysql://dngj:603603@47.116.3.109:3306/finance?charset=utf8mb4')
    df.to_sql(name=name,con = engine,schema='finance',if_exists = method ,index=False)
    return 

def get_data(table_name):
    """输入表名获取数据"""
    conn = pymysql.connect(
    host = '47.116.3.109',	
    user = 'dngj',	
    passwd = '603603',	
    db = 'finance',	
    port=3306,	
    charset = 'utf8mb4'	
    )
    excu="select * from "
    table_name=table_name
    dff = pd.read_sql(excu+table_name,conn)
    return dff

def get_latest_date(table_name):
    """"""
    conn = pymysql.connect(
    host = '47.116.3.109',	
    user = 'dngj',	
    passwd = '603603',	
    db = 'finance',	
    port=3306,	
    charset = 'utf8mb4'	
    )
    excu="select * from "
    table_name=table_name
    dff = pd.read_sql(excu+table_name,conn)