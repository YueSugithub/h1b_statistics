
# coding: utf-8

# In[1]:


import csv
import sys
from collections import Counter

dir_input = sys.argv[1]
dir_occupations = sys.argv[2]
dir_states = sys.argv[3]

# In[2]:


# input and get names of fields
with open(dir_input ,newline='' ,encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter= ';', quotechar=' ')
    rows = [row for row in reader]
    col = rows[0]


# In[3]:


# find the rows which miss data
q = []
for i in range(len(rows)):
    if(len(rows[i]) !=len(col)):
        q.append(i)


# In[4]:


#get the number of certified applications and pick out these applications

n = 0
apps = []

for i in range(len(col)):
    if col[i].endswith( 'STATUS'):
        for j in range(len(rows)):
            if j not in q:
                if rows[j][i] == 'CERTIFIED':
                    n = n+1
                    app = rows[j]
                    apps.append(app)


# In[5]:


#get the columns of worksite state and soc name

a = 0
b = 0 

for i in range(0,len(col)):
    if (col[i].endswith( 'WORKSITE_STATE')):
        a = i
    elif(col[i].endswith( 'SOC_NAME')):
        b = i


# In[6]:


#  remove the quotes in the filed of name to make the data in order

for j in range(len(rows)):
    if rows[j][b].endswith( '\"'):
        rows[j][b] = rows[j][b].strip('\"')
        rows[j][b] = rows[j][b].rstrip('\"')


# In[7]:


#choose top ten occupations

#top ten occupations
occupations =  []
for k in range(len(apps)):
    if k not in q:
        occupation = apps[k][b]
        occupations.append(occupation)

occupations_counts = Counter(occupations)
occupations_counter_new = sorted(occupations_counts.items(), key=lambda x: (-x[1], x[0]))
top_ten_occupations = occupations_counter_new[:10]


#top ten states

states = []
for k in range(len(apps)):
    if k not in q:
        state = apps[k][a]
        states.append(state)


states_counts = Counter(states)
states_counter_new = sorted(states_counts.items(), key=lambda x: (-x[1], x[0]))
top_ten_states = states_counter_new[:10]


# In[8]:


#compute the persentage 

#top ten occupations
top_ten_occupations_per = []
c = min(10,len(top_ten_occupations))
for m in range(c):
    persentage = '%.1f%%' %(100*top_ten_occupations[m][1]/n)
    per = [top_ten_occupations[m][0],top_ten_occupations[m][1],persentage]
    top_ten_occupations_per.append(per)


#top ten states
top_ten_states_per = []
d =  min(10,len(top_ten_states))
for m in range(d):
    persentage = '%.1f%%' %(100*top_ten_states[m][1]/n)
    per = [top_ten_states[m][0],top_ten_states[m][1],persentage]
    top_ten_states_per.append(per)



# In[9]:


#output

#set field on each line is separated by a semicolon 
csv.register_dialect('MyDialect', delimiter=';',doublequote=False,quotechar='',lineterminator='\n',escapechar='',quoting=csv.QUOTE_NONE)


#top ten occupations

with open(dir_occupations,"w") as csvfile: # "top_10_occupations.txt" to dir variable dir_occupations
    writer = csv.writer(csvfile,dialect='MyDialect')


    writer.writerow(["TOP_OCCUPATIONS","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"])
    writer.writerows(top_ten_occupations_per)

#top ten states
with open(dir_states,"w") as csvfile:  # "top_10_states.txt" to dir variable dir_states
    writer = csv.writer(csvfile,dialect='MyDialect')
    
    writer.writerow(["TOP_STATES","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"])
    writer.writerows(top_ten_states_per)

