import mysql.connector
import streamlit as st

#connection

conn=mysql.connector.connect(

    host="localhost",
    port="3306",
    user="root",
    passwd="Lithishrnaik@123",
    db="my_streamlit"
)
c=conn.cursor()


#fetch

def view_all_data():
 c.execute('select * from insurance order by id asc')
 data=c.fetchall()
 return data

