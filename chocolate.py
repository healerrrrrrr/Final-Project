
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
# show the title
st.title('Chocolate Bar by Yuxin Ou and Qiunian Li')
# read csv and show the dataframe

df = pd.read_csv('chocol.csv')
st.subheader('See more filers in the table:')
df


cocoa_percent_filter = st.slider('Median Cocoa Percent :', 40, 70, 100) 

bar_name_filter = st.sidebar.multiselect(
     'Choose the company location',
     df.company_location.head(15).unique(),  # options
     df.company_location.head(15).unique())

bar_name_filter = st.sidebar.multiselect(
     'Choose the specific bean origin',
     df.country_of_bean_origin.head(15).unique(),  # options
     df.country_of_bean_origin.head(15).unique())


rate_filter = st.sidebar.radio('Choose the number of companies level',
                                  ('Low','Media','High'))


b = df[df.cocoa_percent<= cocoa_percent_filter]

if  rate_filter == 'Low':
    c = b[b.rating < 3]
if rate_filter == 'Medium':
    c = b[(b.rating >= 3) & (b.rating < 4)]
if rate_filter == 'High':
    c = b[b.rating>=4]


#st.subheader('The Map')
st.map(df)

st.subheader('Total Rate By Companies')
fig, ax = plt.subplots(figsize=(15, 10))
df.company_location.value_counts().head(15).plot.pie(autopct = '%1.2f%%',
    explode = [0,0,0,0,0,0.3,0,0,0,0,0,0,0,0,0],
    shadow = True,
    colors = ['goldenrod','tan','gold','darkkhaki','wheat']
)
st.pyplot(fig)

st.subheader('The  histogram of Country_of_bean_origin')
fig3, ax = plt.subplots(figsize=(20, 10))
df.country_of_bean_origin.head(15).hist(bins=8, color = 'plum')
st.pyplot(fig3)

st.subheader('The chartr sorted by Cocoa_percent')
a=df.sort_values(by = 'cocoa_percent', ignore_index= 'True',ascending= False)
a


st.subheader('The Line Chart of the Cocoa_percent')
fig1, ax = plt.subplots(figsize=(20, 15))
cocoa_percent = df.sort_values(by = 'cocoa_percent', ignore_index= 'True',ascending= False)
cocoa_percent.cocoa_percent.plot(color = 'seagreen').set_ylabel('Cocoa_percent')
st.pyplot(fig1)


st.subheader('The relationship of the mount of ingredients and rating of cocoa')
fig2, ax = plt.subplots(2, 3, figsize = (15,10))
df[df['counts_of_ingredients'] == 1]['rating'].plot.box(ax = ax[0,0],color = 'red')
df[df['counts_of_ingredients'] == 2]['rating'].plot.box(ax = ax[0,1],color = 'tomato')
df[df['counts_of_ingredients'] == 3]['rating'].plot.box(ax = ax[0,2],color = 'salmon')
df[df['counts_of_ingredients'] == 4]['rating'].plot.box(ax = ax[1,0],color = 'coral')
df[df['counts_of_ingredients'] == 5]['rating'].plot.box(ax = ax[1,1],color = 'hotpink')
df[df['counts_of_ingredients'] == 6]['rating'].plot.box(ax = ax[1,2],color = 'crimson')


ax[0,0].set_ylabel('Rating')
ax[1,0].set_ylabel('Rating')
ax[0,0].set_xlabel('ingredients1')
ax[0,1].set_xlabel('ingredients2')
ax[0,2].set_xlabel('ingredients3')
ax[1,0].set_xlabel('ingredients4')
ax[1,1].set_xlabel('ingredients5')
ax[1,2].set_xlabel('ingredients6')
st.pyplot(fig2)

     




