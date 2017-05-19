#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:50:56 2017

@author: stephanosarampatzes
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('vgsales.csv')

# NA's
df.isnull().sum()

# poses platformes yparxoun?
len(df.Platform.unique())

# outlier ?
df.loc[(df['Year']>2017)]

# ποια κονσολα εχει τα περισσοτερα παιχνιδια DONE

df.Platform.value_counts()

sns.countplot(x='Platform',data=df)
plt.xticks(rotation=90,fontsize=9)
plt.show()

# ποια χρονια βγηκαν τα περισσοτερα παιχνιδια DONE
df.Year.value_counts()

sns.countplot(x='Year',data=df)
plt.xticks(rotation=90,fontsize=9)
plt.show()

# ποια χρονια βγηκαν τα πιο πολλα φραγκα DONE

groupGlobal=df[['Year','Global_Sales']].groupby(['Year'],as_index=False).sum()

sns.barplot(x='Year' ,y='Global_Sales' ,data=groupGlobal,palette='GnBu_d')
plt.xticks(rotation=90)
plt.xlabel('Year')
plt.ylabel('Global Sales')
plt.show()

# ποια χρονια εβγαλε καθε εταιρεια τα περισσοτερα παιχνιδια σε ολες τις κονσολες.

#group=df[['Publisher','Year']].groupby(['Year']).count()
#group2=df[['Publisher','Year']].groupby(['Publisher']).max()
#group2_2=df[['Platform','Year']].groupby(['Year'],as_index=False).sum()

group2_3=df[['Publisher','Year']].groupby(['Year'],as_index=False).sum()


bspy=df[['Publisher','Year']].groupby(['Year'],as_index=False).agg(lambda x:x.value_counts().index[0])

#bspy2=df[['Platform','Year']].groupby(['Year'],as_index=False).agg(lambda x:x.value_counts().index[0])

sns.barplot(x='Publisher',y='Year',data=bspy)








# Top 20 περισσοτερες πωλησεις ever ανα publisher DONE
global_=df[['Global_Sales','Publisher']].groupby(['Publisher'],as_index=False).sum().sort_values(['Global_Sales'],ascending=False)
global_= global_.nlargest(20, ['Global_Sales','Publisher'])

sns.barplot(global_.Publisher,global_.Global_Sales,data=global_)
plt.ylabel('Gloabal Sales in millions')
plt.xlabel('Publishers')
plt.xticks(rotation=90)
plt.title("Top 20 Publisher Global Sales")
plt.show()

# top sales / territory DONE

total_territory=df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]    
total_territory.sum(axis=0)
sns.barplot(x=total_territory.columns.values,y=total_territory.sum(axis=0))

# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    total_territory,
    # with the labels being officer names
    #labels=df['officer_name'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()




# DONE
total_sales = df.groupby('Year').agg({'Global_Sales': np.sum, 'NA_Sales': np.sum,
                      'EU_Sales': np.sum, 'JP_Sales': np.sum, 'Other_Sales': np.sum})
plt.plot(total_sales.Global_Sales, label='Global')
plt.plot(total_sales.NA_Sales, label='North America')
plt.plot(total_sales.EU_Sales, label='Europe')
plt.plot(total_sales.JP_Sales, label='Japan')
plt.plot(total_sales.Other_Sales, label='Other_Sales')
plt.ylabel('Sales in Millions')
plt.legend(loc='upper left')
plt.xlabel('Year',fontsize=13)
plt.title('Total sales of regions per year')
plt.show()



# most popular genre DONE

print(df.Genre.value_counts())
sns.countplot(x=df['Genre'].sort_values(),data=df,palette='flatui')
plt.xticks(rotation=60)
plt.title('Most popular genre based on releases (alphabetical order)')
plt.show()

  
sale1 = []

for i in df['Genre'].unique():
    sale1.append(df[df['Genre'] == i]['Global_Sales'].sum())    
    
sns.barplot(x = df['Genre'].unique(),y = sale1)
plt.xticks(rotation=60)
plt.xlabel('Genre',fontsize=13)
plt.ylabel('Global Sales in millions',fontsize=13)
plt.title('Sales / Genre',fontsize=15)
plt.show()


# best selling platforms DONE
sale2=[]
for i in df['Platform'].unique():
    sale2.append(df[df['Platform']==i]['Global_Sales'].sum())

sns.barplot(x=df['Platform'].unique(),y=sale2)    
plt.xticks(rotation=60)
plt.xlabel('Platform')
plt.ylabel('Global Sales')
plt.title('Global Sales for each Platform')
plt.show()

# Best sales per year / publisher

platform_sales=df[[]].groupby('Year')


# max global sales per platform

sale3=[]
year=[]
platforms=[]
platforms=np.array(platforms)
plats=[]

for i in df['Year'].unique():
    print(i)
    print(df[df['Year']==i]['Global_Sales'].max())
    sale3.append(df[df['Year'] == i]['Global_Sales'].max()) 
    year.append(i)
    print(df[df['Year']==i]['Platform'].unique())
    platforms.append(df[df['Year']==i]['Platform'].unique())
    
    #platforms = platforms[np.logical_not(np.isnan(platforms))]

for j in range(len(platforms)):
    print(platforms[j][0])
    plats.append(platforms[j][0])

'''
myset = set(year)
print(myset)
for i in df['Platform'].unique():
    platforms.append(i)
'''

from matplotlib.pyplot import show
ax=sns.barplot(x=df['Year'].unique(),y=sale3,data=df)    
plt.xticks(rotation=90)
rects = ax.patches

# Now make some labels
#labels = ["label%d" % i for i in range(len(rects))]
labels=df['Platform'].unique()
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height+0.5 , label,rotation=90, ha='center', va='bottom',)

plt.show()

# total global sales / platform DONE

new_group=df.groupby(['Platform'],as_index=False).sum().drop(['Rank','Year'],axis=1)
sns.barplot(x='Platform', y='Global_Sales', data=new_group)
plt.xticks(rotation=90)
plt.show()
# sales per region / platform DONE
regions=['NA_Sales','EU_Sales','JP_Sales','Other_Sales']
subs=[1,2,3,4]
fig,ax = plt.subplots(figsize=(12, 11))
for i,j in zip(regions,subs):
    plt.subplot(3,2,j)
    sns.barplot(x='Platform',y=i,data=new_group);
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# πωλησεις ανα περιοχη στις κονσολες  DONE


r11=sns.barplot(x='Platform', y='NA_Sales', data=new_group, color = '#04d8b2')
r22=sns.barplot(x='Platform', y='EU_Sales', data=new_group, color = '#75bbfd')
r33=sns.barplot(x='Platform', y='JP_Sales', data=new_group, color='#c0fb2d')
r44=sns.barplot(x='Platform', y='Other_Sales', data=new_group, color='#cf6275')


NA = plt.Rectangle((0,0),1,1,fc='#04d8b2', edgecolor = 'none')
EU = plt.Rectangle((0,0),1,1,fc='#75bbfd',  edgecolor = 'none')
JP = plt.Rectangle((0,0),1,1,fc='#c0fb2d',  edgecolor = 'none')
Other = plt.Rectangle((0,0),1,1,fc='#cf6275',  edgecolor = 'none')

l = plt.legend([NA, EU, JP, Other], ['NA', 'EU', 'JP', 'Other'], loc=2, ncol = 2, prop={'size':10})
l.draw_frame(False)

sns.despine(left=True)
plt.xticks(rotation=60)
r11.set_ylabel('Sales/Region (millions)')
r11.set_xlabel('Platform')
r11.set_title('Sales per Region / Platform')

#---------------
# πωλησεις ανα περιοχη στα ειδη παιχνιδιων  DONE

new_group2=df.groupby(['Genre'],as_index=False).sum().drop(['Rank','Year'],axis=1)



r1=sns.barplot(x='Genre', y='NA_Sales', data=new_group2, color = '#0485d1')
r2=sns.barplot(x='Genre', y='EU_Sales', data=new_group2, color = '#ff474c')
r3=sns.barplot(x='Genre', y='JP_Sales', data=new_group2, color='#d2bd0a')
r4=sns.barplot(x='Genre', y='Other_Sales', data=new_group2, color='#5ca904')


NA = plt.Rectangle((0,0),1,1,fc='#0485d1', edgecolor = 'none')
EU = plt.Rectangle((0,0),1,1,fc='#ff474c',  edgecolor = 'none')
JP = plt.Rectangle((0,0),1,1,fc='#d2bd0a',  edgecolor = 'none')
Other = plt.Rectangle((0,0),1,1,fc='#5ca904',  edgecolor = 'none')

l = plt.legend([NA, EU, JP, Other], ['NA', 'EU', 'JP', 'Other'], loc=1, ncol = 2, prop={'size':10})
l.draw_frame(False)

sns.despine(left=True)
plt.xticks(rotation=60)
r1.set_ylabel('Sales/Region (millions)')
r1.set_xlabel('Genre')
r1.set_title('Sales per Region / Genre')

#----------------------------------------------------------------------

#publishers with >100 counts  DONE
df['Counts'] = df.groupby(['Publisher'])['Name'].transform('count')

groupPR = df.groupby(['Counts','Publisher'],as_index=False).sum().sort_values('Counts',ascending=False)
groupPR=groupPR[:29]

#drop unknown publisher
groupPR=groupPR.drop([561])

groupPR['origin']=groupPR.Publisher.replace({'Electronic Arts' :'US','Activision' :'US','THQ' :'US','Take-Two Interactive' :'US','Warner Bros. Interactive Entertainment' :'US',
       'Disney Interactive Studios' :'US','Midway Games' :'US','Microsoft Game Studios' :'US','Acclaim Entertainment' :'US','Vivendi Games' : 'US','Namco Bandai Games' :'JP',
       'Konami Digital Entertainment' :'JP','Nintendo' :'JP','Sony Computer Entertainment' :'JP','Sega' :'JP','Capcom' :'JP','Tecmo Koei' :'JP','Square Enix' :'JP','D3Publisher' :'JP',
       'Idea Factory' :'JP','Nippon Ichi Software' :'JP','Ubisoft' :'EU','Atari' :'EU','Eidos Interactive' :'EU','505 Games' :'EU','Codemasters' :'EU','Deep Silver' :'EU',
       'Zoo Digital Publishing' :'EU'})
    
    
sns.barplot(x='Publisher',y='Global_Sales',hue='origin',data=groupPR)
plt.xticks(rotation=90)

team_origin=groupPR.groupby(['origin'],as_index=False).sum()
team_origin=team_origin.drop(['Rank','Year','Counts'],axis=1)
sns.barplot(x='origin', y='Global_Sales', data=team_origin)

regions=['NA_Sales','EU_Sales','JP_Sales','Other_Sales']
subs=[1,2,3,4]
fig,ax = plt.subplots(figsize=(12, 11))
for i,j in zip(regions,subs):
    plt.subplot(3,2,j)
    sns.barplot(x='origin',y=i,data=team_origin)
    plt.tight_layout()
    plt.show()
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

soty = df[['Global_Sales','Year']].groupby(['Year']).max()

soty2=[]
lst=[]
cols=['Platform']
soty3=pd.DataFrame(lst, columns=cols)
soty3=[]

for i in soty.index:
    soty2.append(np.where((df['Year']==i)&(df['Global_Sales']==soty['Global_Sales'][i])))


for i in soty2:
    soty3.append(df.iloc[i]['Platform'])

soty3 = pd.DataFrame({"Platform": soty3})


labels=pd.Series([])
for i in range(1,39):
    labels=labels.append(soty3.Platform[i])

# plot ------

ax = sns.barplot(x=soty.index, y=soty.Global_Sales,data=soty)
plt.xticks(rotation=90,fontsize=13)
plt.xlabel('Year',fontsize=15)
plt.yticks(fontsize=13)
plt.ylabel('Global Sales in millions',fontsize=15)
plt.title('Platform Of the Year in Sales',fontsize=15)
rects = ax.patches

labels=labels

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height+0.5 , label,rotation=90, ha='center', va='bottom',)

plt.show()

#-------------
