import streamlit as sl
import snowflake.connector as sfc
import pandas as pd

sl.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
my_cnx = sfc.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the dafta into a dataframe
df = pd.DataFrame(my_catalog)

# put the first column into a list
color_list = df[0].values.tolist()

# pick list
option = sl.selectbox('Pick a sweatsuit color or style:', list(color_list))

# image caption
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

# get data from db
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where
color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
sl.image(
df2[0],
width=400,
caption= product_caption
)
sl.write('Price: ', df2[1])
sl.write('Sizes Available: ',df2[2])
sl.write(df2[3])
