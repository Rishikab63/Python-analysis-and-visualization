# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:53 2024

@author: Rishika
"""

import pandas as pd
import matplotlib.pyplot as plt

slices=[50, 14, 24, 5]

#dep name
depts=['sales','production','HR','finance']

#set color
cols=['magenta', 'cyan', 'brown', 'yellow']

#create a pie chart
plt.pie(slices,labels=depts,colors=cols)

#set title
plt.title("Bit departments")


plt.show()