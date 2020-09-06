#Entire data which has text value convert into integer value using dataiku
import pandas as pd
data=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQRtMKSAzDVoUFeP_lvpxSPt0pb7YR3_SPBdnq0_2nIgfZUMB8fMgJXaMETqLmrV3uw2yOqkZLEcTvt/pub?output=csv')
data.head(3)

Y=data["price"]
iv=data.columns
iv=iv.delete(0)#remove the price bcz its our outcome
X=data[iv]

#Model1:-Train the model using LinearRegression
from sklearn.linear_model import LinearRegression
from statsmodels.api import OLS

lr=LinearRegression()
lr.fit(X,Y)

#Model2:-Train the Ordinary Least Square Regression
from statsmodels.api import OLS #In OLS we need to reverse of LinearRegression (X,Y)
model=OLS(Y,X).fit()

#Remove Multicollinearity using Varience Inflation Factor

#check the model summary
model.summary()

#calculate the varience inflation factor
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
[vif(data[iv].values,index) for index in range(len(iv))] #compare with each columns

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
for i in range(len(iv)):
    vif_list=[vif(data[iv].values,index) for index in range(len(iv))] #compare with each columns
    maxvif=max(vif_list)
 #   print("Max VIF value is ",maxvif)
    drop_index= vif_list.index(maxvif)
  #  print("For Independent variable",iv[drop_index])
    if maxvif>10:
   #     print("Deleting",iv[drop_index])
        iv=iv.delete(drop_index)
    #    print("Final Independent_variables ",iv)

Y=data["price"]
X=data[iv]
model=OLS(Y,X).fit()

model.summary()

import sys
index = 1
user_input = {}
for var in iv:
  # temp=input("Enter "+var+":")
    temp =sys.argv[index]
    index =index + 1
    user_input[var] = temp
user_df=pd.DataFrame(data=user_input,index=[0],columns=iv)
import sklearn.linear_model as lm
lr=lm.LinearRegression()
lr.fit(X,Y)
price=lr.predict(user_df)
print("House Price is INR ",int(price[0]*75.29))

