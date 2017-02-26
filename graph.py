import numpy as np  
import matplotlib.pyplot as plt  

msl = [2411711, 
2274635, 
2153350, 
2214565, 
2302040, 
1960711, 
2193292, 
2282543, 
2146392, 
2237378, 
2125005, 
2260628, 
2208189, 
2660535, 
2923894, 
2592889, 
2647383, 
2634587, 
2737640, 
2515057
]

visitors = msl.reverse()

year = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

plt.plot(year, msl, 'cd')
plt.show()
poly = np.polyfit(year, msl, 4, rcond=None, full=False, w=None, cov=False)

print(poly[0])
print(poly[1])
print(poly[2])
print(poly[3])
print(poly[4])

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)
    plt.plot(year, msl, 'o')
    plt.title("Visitor Population Trend for Cape Hatteras National Park")
    plt.ylabel("Visitor Population (People)")
    plt.xlabel("Year")
    plt.show()
    

graph('poly[0]*x*x*x*x + poly[1]*x*x*x + poly[2]*x*x + poly[3]*x + poly[4]', range(1997, 2016))