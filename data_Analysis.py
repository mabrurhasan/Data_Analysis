import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('C:\Users\hasan\OneDrive\Desktop\SALES.XLSX')
df.head()
#Adding Calender Attributes and Total Sales Column
df['Tot_SALES']= df['Retail_Sales']+ df['whole_Sales']
#MONTH
df["MONTH"]= df["Actual data"].dt.month
#MONTH_YEAR
df["Month_Year"]=df["Actual Date"].dt.strftime(" %b %y ")
#DAYName
df["Day"]=df["actual Date "].dt.strftime("%A") #if you give small ' a 'then it give sorter day name
#YEAR 
df['Year']=df['Actual Date'].dt.year

df.head()
#YEARLY SALES STATS
year_sales = df.pivot_table(index= "Year", values = "Tol_sales", aggfunc ="sum")
year_sales.reset_index()
y = year_sales['Tol_sales']
#CREATE A PIE CHART
plt.figure(figsize=(8,8))
plt.pie(y,labels= x, autopct ="%.f %%")
plt.title("SALES BY YEARS")
plt.show()
#MONTHLY SALES TREND
monthly_sales = df.pivot_table(index= "Month", values = "Tol_sales", aggfunc ="sum")
monthly_sales = monthly_sales.reset.reset_index()
print(monthly_sales)
x= monthly_sales['Month_year']
y = monthly_sales['tol_sales']
#CREATING BAR GRAPH
plt.figure(figsize=(18,8))
plt.title('Sales by month')
plt.xlabel('Month_Year')
plt.ylabel('Total_sales')
plt.bar(x,y)
plt.xticks(rotation=45)
plt.show()
#BRAND WISE SALES
brand_sales = df.pivot_table(index= "brand", values = "Tol_sales", aggfunc ="sum")
brand_sales = brand_sales.reset.reset_index()
brand_sales = brand_sales.reset.sort_values(by='tol_sales',ascending = False)
print(brand_sales)
x=brand_sales['BRAND']
y = brand_sales['tol_sales']
#CREATING BAR GRAPH
plt.figure(figsize=(18,8))
plt.title(' Brand wise sales')
plt.xlabel('Brand Sales')
plt.ylabel('Total_sales')
plt.bar(x,y)
plt.xticks(rotation = 45)
plt.show()
#Territory wise Sales
territory_sales = df.pivot_table(index= "territory", values = "Tol_sales", aggfunc ="sum")
territory_sales = territory_sales.reset.reset_index()
territory_sales = territory_sales.reset.sort_values(by='tol_sales',ascending = False)
print(territory_sales)
x=territory_sales['BRAND']
y = territory_sales['tol_sales']
#CREATING BAR GRAPH
plt.figure(figsize=(18,8))
plt.title(' territory wise sales')
plt.xlabel('territory Sales')
plt.ylabel('Total_sales')
plt.bar(x,y)
plt.xticks(rotation = 45)
plt.show()
