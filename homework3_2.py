
# coding: utf-8

# In[1]:


import math
import random                     
import matplotlib.pyplot as plt    

n_trials = 15500  #change n               
n_inside = 0
inside_x = []
inside_y = []
outside_x = []
outside_y = []
p_max = 1-math.exp(-1) 
for i in range(n_trials):
    x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0) *p_max
    p_x = 1-math.exp(-x)
    if  p_x > y: 
        n_inside += 1
        inside_x.append(x)
        inside_y.append(y) 
    else:
        outside_x.append(x) 
        outside_y.append(y) 


plt.plot(inside_x, inside_y, 'x' )
plt.plot (outside_x, outside_y, '.')
plt.show()
print ("Integral approx = ", p_max * n_inside / float(n_trials))


# In[8]:


import random                     
import matplotlib.pyplot as plt    
import math              
n_estimat= 1000
integ=math.exp(-1)
s=0
n_trials=1000

for j in range (n_estimat):     
    n_inside = 0
    for i in range(n_trials):
        x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0) *p_max
        p_x = 1-math.exp(-x)
        if  p_x > y: 
            n_inside += 1
    m= p_max * n_inside / float(n_trials)
    #print (m)
    s+= (m - integ)*(m-integ) 
s/= n_estimat
error=math.sqrt(s)
print ('Error is ', s)
#plt.p


# In[3]:


import random 
import math 
import matplotlib.pyplot as plt 

x_dat=[]
y_dat=[]
N=2300
for i in range (N):
    z=random.uniform(0.0, 1.0) 
    x=math.sqrt(z) 
    x_dat.append(x)
    px=2*x
    y=random.uniform(0.0,0.5*px)
    y_dat.append(y)

a_dat=[]
b_dat=[]

for i in range (N):
    a=random.uniform(0.0, 1.0) 
    b=random.uniform(0.0,a)
    a_dat.append(a)
    b_dat.append(b)
print (len(x_dat), len(y_dat))
plt.plot([0,1], [0,1])
plt.plot(x_dat,y_dat,'x')
plt.show()


plt.plot([0,1], [0,1])
plt.plot(a_dat,b_dat,'x')
plt.show()


# In[4]:


import math
import random                     
import matplotlib.pyplot as plt    

n_trials = 15500  #change n               
n_inside = 0
inside_x = []
inside_y = []
outside_x = []
outside_y = []
p_max = 1-math.exp(-1) 

for i in range(n_trials):
    z=random.uniform(0.0, 1.0) 
    x=math.sqrt(z)
    px=2*x
    y=random.uniform(0.0,0.5*px)
    p_x = 1-math.exp(-x)
    if  p_x > y: 
        n_inside += 1
        inside_x.append(x)
        inside_y.append(y) 
    else:
        outside_x.append(x) 
        outside_y.append(y) 


plt.plot(inside_x, inside_y, 'x' )
plt.plot (outside_x, outside_y, '.')
plt.plot([0,1], [0,1])
plt.show()
print ("Integral approx = ", 0.5 * n_inside / float(n_trials))


# In[12]:


import random                     
import matplotlib.pyplot as plt    
import math              
n_estimat= 100
integ=math.exp(-1)
s=0
error_2=[]
error_1=[]

for n_trials in range (800,850):
    s1=0
    s2=0
    for j in range (n_estimat):     
        n_inside1 = 0
        n_inside2=0
        for i in range(n_trials):
            #method 1 
            x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0) *p_max
            p_x = 1-math.exp(-x)
            if  p_x > y: 
                n_inside1 += 1
            #method 2
            z=random.uniform(0.0, 1.0) 
            x=math.sqrt(z)
            px=2*x
            y=random.uniform(0.0,0.5*px)
            p_x = 1-math.exp(-x)
            if  p_x > y: 
                n_inside2 += 1
        m1= p_max * n_inside1 / float(n_trials)
        s1+= (m1 - integ)*(m1-integ)
    
        m2= 0.5 * n_inside2 / float(n_trials)
        s2+= (m2 - integ)*(m2-integ)
    s1/= n_estimat
    er1=math.sqrt(s1)
    error_1.append(er1)                       
    s2/= n_estimat
    er2=math.sqrt(s2)
    error_2.append(er2)
    

plt.plot (range(50),error_1,label='Method 1')
plt.plot (range(50),error_2, label= 'Method 2')
plt.legend(loc='center right')
plt.xlabel('n')
plt.ylabel('Error')
plt.show()                          


# In[11]:


import math
import random                     
import matplotlib.pyplot as plt    

n_trials = 15500  #change n               
n_inside = 0
inside_x = []
inside_y = []
outside_x = []
outside_y = []
p_max = 1-math.exp(-1) 
c=(2/3)*p_max
a_tot= p_max * (2/3)
for i in range(n_trials):
    z=random.uniform(0.0, 1.0) 
    x=z**(2/3)
    px=(3/2)*x**(1/2)
    y=random.uniform(0.0,c*px)
    p_x = 1-math.exp(-x)
    if  p_x > y: 
        n_inside += 1
        inside_x.append(x)
        inside_y.append(y) 
    else:
        outside_x.append(x) 
        outside_y.append(y) 


plt.plot(inside_x, inside_y, 'x' )
plt.plot (outside_x, outside_y, '.')
plt.plot([0,1], [0,1])
plt.show()
print ("Integral approx = ", a_tot * n_inside / float(n_trials))


# In[15]:


import random                     
import matplotlib.pyplot as plt    
import math              
n_estimat= 100
integ=math.exp(-1)
s=0
error_2=[]
error_1=[]
error_3=[]
p_max = 1-math.exp(-1) 
c=(2/3)*p_max
a_tot= p_max * (2/3)
for n_trials in range (800,850):
    s1=0
    s2=0
    s3=0
    for j in range (n_estimat):     
        n_inside1 = 0
        n_inside2=0
        n_inside3=0
        for i in range(n_trials):
            #method 1 
            x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0) *p_max
            p_x = 1-math.exp(-x)
            if  p_x > y: 
                n_inside1 += 1
            #method 2
            z=random.uniform(0.0, 1.0) 
            x=math.sqrt(z)
            px=2*x
            y=random.uniform(0.0,0.5*px)
            p_x = 1-math.exp(-x)
            if  p_x > y: 
                n_inside2 += 1
            #method 3 
            z=random.uniform(0.0, 1.0) 
            x=z**(2/3)
            px=(3/2)*x**(1/2)
            y=random.uniform(0.0,c*px)
            p_x = 1-math.exp(-x)
            if  p_x > y: 
                n_inside3 += 1
                
        m1= p_max * n_inside1 / float(n_trials)
        s1+= (m1 - integ)*(m1-integ)
    
        m2= 0.5 * n_inside2 / float(n_trials)
        s2+= (m2 - integ)*(m2-integ)
        
        m3= a_tot * n_inside3 / float(n_trials)
        s3+= (m3 - integ)*(m3-integ)
        
    s1/= n_estimat
    er1=math.sqrt(s1)
    error_1.append(er1)                       
    s2/= n_estimat
    er2=math.sqrt(s2)
    error_2.append(er2)
    s3/= n_estimat
    er3=math.sqrt(s3)
    error_3.append(er3)
    

plt.plot (range(50),error_1,label='Method 1')
plt.plot (range(50),error_2, label= 'Method 2')
plt.plot (range(50),error_3, label= 'Method 3')
plt.legend(loc='center right')
plt.xlabel('n')
plt.ylabel('Error')
plt.show()                      

