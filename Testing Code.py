##print (df)
a = 5
b = 3
print(a + b)
import pandas as pd
##dfxlsx = pd.read_excel ('/home/redhwanzaman1989/Python Data Analysis/Dummy RWA Data.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
##dfxls  = pd.read_excel ('/home/redhwanzaman1989/Python Data Analysis/Dummy RWA Data.xls') #for an earlier version of Excel, you may need to use the file extension of 'xls'
##no_pat = pd.read_excel('Dummy RWA Data.xlsx') 
##print(dfxlsx)
##print(dfxls)
##print(no_pat)

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()