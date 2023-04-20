import streamlit
streamlit.title('MY PARENTS NEW HEALTHY DINER')


streamlit.header('BREAKFAST MENU')
streamlit.text('🥣 OMEGA 3 & BLUEBERRY OATMEAL')
streamlit.text('🥗 KALE, SPINACH & ROCKET SMOOTHIE')
streamlit.text('🐔HARD-BOILED FREE-RANGE EGG')
streamlit.text('🥑🍞 AVOCADO TOAST')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


