import streamlit as sl
import snowflake.connector as sfc

my_cnx = sfc.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
sl.text("Hello from Snowflake:")
sl.text(my_data_row)
