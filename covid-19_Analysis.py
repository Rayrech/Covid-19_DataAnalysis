#importing req libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#upload data files
data = pd.read_csv("Covid cases in India.csv")
data.head()

#cheack frames created with pandas
data.info()
#name columns
data.rename(columns={'Name of State / UT':'States','Cured/Discharged Migrated':'Discharged'},inplace=True)
data.columns

#cleaning the data
data.isnull().sum()
x=data["Active"].mode()[0]
print(x)
data["Active"].fillna(x,inplace=True)
data.head(20)

data.isnull().sum()

#add columns to get the information about percentages
data['%cured'] = (data['Discharged']/data['Total Confirmed cases'])*100
data['%Deaths']=(data['Deaths']/data['Total Confirmed cases'])*100
data['%Active']=(data['Active']/data['Total Confirmed cases'])*100
#print(data['%cured'])
#print(data['%Deaths'])
df_latest = data.sort_values(by=['%cured'], ascending = False)
df_latest.head(10)

print("The total no of deaths:",df_latest['Deaths'].sum())
print("The total no of cured:",df_latest['Discharged'].sum())

#create a colour gradient graph 
df2= df_latest.copy()
df_Top= df2.head(10)
df_Top.style.background_gradient(cmap='Reds')


#Bar graph where
df2 = df_latest.sort_values(by=['Total Confirmed cases'], ascending = False)
for feature in df2[['Total Confirmed cases','Discharged','Deaths','Active']]:
  fig=plt.figure(figsize=(50,10))
  plt.title("Top 10 states", size=10)
  ax=sns.barplot(data=df2,y= df2[feature],x='States', linewidth=0, edgecolor='black')
  plt.xlabel('States', size = 15)
  plt.ylabel(feature, size = 15)
for i in ax.patches:
  ax.text(x=i.get_x(),y=i.get_height(),s=i.get_height())
  plt.show()

#upload 2nd data file (per day data)
day = pd.read_csv("per_day_cases.csv")
print(day)

#line graph to track the patteren in the new cases
plt.figure(figsize=(100,5))
sns.lineplot(x="Date",y="New Cases",data=day,color="r",lw=3,marker='o',markersize=10)
plt.title('RATE OF CASES ')
plt.show()

#upload vaccination details data
vacc = pd.read_csv("COVID-19 India Statewise Vaccine Data.csv")
vacc.head(15)

#bar graph comparing vaccination per state
vacc_new = vacc.sort_values(by=['Dose 1'], ascending = False)
plt.figure(figsize=(25,4))
plt.bar(vacc_new['State/UTs'][:15], vacc_new['Dose 1'][:15],align='center',color='skyblue')
plt.xlabel('states', size = 12)
plt.ylabel('Vaccination Doses', size = 12)
plt.title('Statewise dose 1', size = 16)
plt.show()


#line graphs comparing 1st and 2nd dose
plt.figure(figsize=(15,5))
sns.lineplot(x="State/UTs",y="Dose 1",data=vacc.tail(10),color="g",lw=3,marker='o',markersize=10)
plt.title('RATE OF vaccination of each state')
plt.show()

plt.figure(figsize=(15,5))
sns.lineplot(x="State/UTs",y="Dose 2",data=vacc.tail(10),color="g",lw=3,marker='o',markersize=10)
plt.title('RATE OF vaccination of each state')
plt.show()