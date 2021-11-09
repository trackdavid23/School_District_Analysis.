#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os

school_load = os.path.join(r"/Users/bigd/Downloads/Columbia\ Bootcamp/School\ District\ Analysis/schools_complete.csv")
student_load = os.path.join(r"/Users/bigd/Downloads/Columbia\ Bootcamp/School\ District\ Analysis/students_complete.csv") 

school_data_df = pd.read_csv(school_load)
school_data_df.head()


# In[ ]:


# List of high schools
high_schools = ["Hernandex High School","Figueroa High School",
               "Wilson High School","Wright High School","Shelton High School", 
                "Hernandez High School","Griffin High School","Wilson High School",
                "Cabrera High School", "Bailey High School", "Holden High School",
                "Pena High School", "Wright High School","Rodriguez High School",
                "Johnson High School", "Ford High School", "Thomas High School"]
for school in high_schools:
    print(school)
    
#A dictionary of high schoolsna and the type of school.
high_school_types = [{"High School": "Griffin","Type":"District"},
                     {"High School": "Figueroa","Type":"District"},
                     {"High School": "Wilson","Type":"Charter"},
                     {"High School": "Wright","Type":"Charter"}]
school_series = pd.Series(high_schools)
school_series


# In[ ]:


high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]


# In[ ]:


school_df = pd.DataFrame(high_school_dicts)
school_df


# In[ ]:


# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]

type_of_school = ["District", "District", "Charter", "District","Charter"]


# In[ ]:


# Initialize a new DataFrame.
schools_df = pd.DataFrame()
# Add the list to a new DataFrame.
schools_df["School ID"] = school_id
schools_df["School Name"] = school_name
schools_df["type_of_school"] = type
# Print the DataFrame.
schools_df


# In[ ]:


high_schools_dict = {'School ID': school_id, 'school_name':school_name, 'type':type_of_school}


# In[ ]:


school_df.columns


# In[ ]:


school_df.index
#to get indices use df.index just add to the dataframe


# In[ ]:


school_df.values


# In[ ]:





# In[ ]:




