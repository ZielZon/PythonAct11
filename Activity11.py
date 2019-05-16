import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = pd.read_csv("tips.csv") 

tips["total_bill_with_tips"] = (tips["tip"] + tips["total_bill"])


smokers = tips[tips.smoker == "Yes"]
non_smokers = tips[tips.smoker == "No"]
corr = tips.corr()['total_bill'][:]
print(corr)

print("As you can see only the added column total_bill_with tips has a strong correlation with the total_bill")
print("")

smokers = smokers.sort_values(['total_bill'])
non_smokers = non_smokers.sort_values(['total_bill'])
plt.plot(smokers['total_bill'], smokers['tip'])
plt.plot(non_smokers['total_bill'], non_smokers['tip'])
plt.legend(['Smokers', 'Non-Smokers'])
plt.xlabel('Total Bill in R')
plt.ylabel('Tip in R')
plt.title('Smokers Tipping vs Non-Smokers')
plt.show()
