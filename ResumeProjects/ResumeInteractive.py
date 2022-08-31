# %% [markdown]
# # Personal Information

# %% [markdown]
# Cole B. Hamilton 
# 
# Senior Data Analyst 
# 
# San Antonio, TX 
# 
# cbhami02@louisville.edu
# 
# www.linkedin.com/in/hamiltoncole/
# 
# www.github.com/cbhami/Coraline/

# %% [markdown]
# Self-driven professional with excellent writing skills with mastery managing analysts, recruitment training, and agile team building in United States Army. Flexible and devoted professional used to a fast-paced environment where solving problems is crucial. Well-versed in the use of statistical analysis and data analysis to identify underperforming areas and manage courses to increase junior members. Proven record in data analysis cleaning, visualizing, automating, and presenting complex datasets for senior managers. Mastery of data analytics reporting through data programming languages, quantitative analysis, statistical analysis, and dashboard creations. Maintained data solutions, data security, and protected information data governance.

# %% [markdown]
# ## *Skills* 
# 
# ---
# 

# %% [markdown]
# ●	Master in Agile Project Management, Human Resources, Leadership, and Staff Development.
#  
# ●	Highly advanced skills in data cleaning, data visualization, and report construction. 
# 
# ●	Experienced in content design, virtual teaching, and development. Expert in MS Teams.
#  
# ●	Proficient in R, Python, M, DBA, and DAX programming languages.
# 

# %% [markdown]
# ## *Professional Experience* 
# 
# ---
# 
# 

# %% [markdown]
# 
# ### ***Senior Data Analyst - 					July 2020 - Present*** 
# 
# ---
# 
# 
# 
# ●	Senior Data Analyst for the largest of five brigades within the United States Army Recruiting Command. Architected and maintained data analytics models, reports, and dashboards for the command team.
# 
# ●	Design and facilitate the use of Power Bi, r Studio, and Microsoft Excel analytical tools. Executed Power Query scripts and established tools for a team of 2,400 Soldiers to utilize.
# 
# ●	Manages millions of rows of code using SQL and database connections to provide data analytics to senior Army leaders; improved production efficiencies across 250 recruiting stations.
# 
# ●	Trained a staff of seven operations analysts and five training professionals to transform the regional headquarters in advanced Microsoft Excel and Power Bi report development. 
# 
# ●	Established the 8-page Mission Report - updated and published daily with code pulled from Open Database Connectivity through R, SQL, M, and DAX scripting languages. 
# 
# ●	Enabled senior leaders to make data driven decisions through technical writing and strategic business analysis.
# 
# ●	Collaborated with regional developers and data engineers to produce data road maps to develop over two-hundred successful business intelligence reports and products delivered to the general.
# 

# %% [markdown]
# ## *Leadership and Training Management Experience* 
# 
# 
# ---

# %% [markdown]
# ### ***District Recruiting Manager							May 2018 - July 2020*** 
# 
# ---
# 
# 
# 
# ●	Served as the Senior Enlisted Advisor facilitating one of three companies covering all enlisted accessions and officer commissioning in Iowa. 
# 
# ●	Advised the commander on briefings, public engagements, marketing opportunities, and onboarding processes for a team of 30 Soldiers. 
# 
# ●	Upskilled over 30 senior army leaders in business solutions and business decision making through managing annual evaluations, awards and commendations, counseling, and mentoring. 
# 
# ●	Generated business insights through data exploration and business intelligence methods. 
# 
# ●	Developed campaign strategies and used technical skills to interpret data for the commander. 
# 
# ●	Conducted management consulting for six other companies within the region while balancing simultaneous projects and meeting business demands.
# 
# ●	Conceptualized, analyzed data, and evaluated recruiting operations to support a company for combined annual enlistment objectives of over 210 hires.
# 
# ●	Led Soldiers in a unit consisting of over 30 hiring counselors and subordinate office managers. Focused strategic initiatives to achieve success. 
# 

# %% [markdown]
# ### ***Senior Noncommissioned Officer					October 2004 - May 2018*** 
# 
# ---
# 
# 
# 
# ●	Senior manager in human resources with a focus in technical teams and process improvements in Army recruiting methods for over 200 direct and indirect reports.
# 
# ●	User friendly leader with over 12 years of human resource and technical recruiting expertise. 
# 
# ●	Proven skill to execute tasks in a team environment and rise as a leader amongst peers.
# 
# ●	Delivered service autonomously as an overseas recruiter assigned to Heidelberg MEPS covering three continents. 
# 
# ●	Interacted with over 20 NATO, UN, and DOD component installations along with 5 US Embassies across the world. Motivated a small geographically dispersed team to collaborate and problem solve to achieve business requirements.
# 
# ●	Performed as a Paratrooper and Engineer with the 82nd Airborne Division in both Operation Enduring and Operation Iraqi Freedom. 
# 
# ●	Formed and managed teams with diverse people through effective communication, conflict management, and social intelligence. Displayed skills in leadership and people management while planning special projects.
# 

# %% [markdown]
# ## *Education*

# %% [markdown]
# Graduate Certificate in Data Science (Est May 2023)
# 
# - University of Louisville, KY
# 
# Doctor of Philosophy, Human Resource Management (GPA 3.77) 
# - Northcentral University, La Jolla, CA 
# 
# Master of Arts, Leadership and Management (GPA 3.5) 
# - Liberty University, Lynchburg, VA 
# 
# Master of Business Administration in Finance (GPA 3.82) 
# - Post University, Waterbury, CT 
# 

# %% [markdown]
# ## *Certifications*

# %% [markdown]
# SHRM-CP Society for Human Resource Management – Senior Certified Professional
# 
# PMI-DASSM Disciplined Agile Senior Scrum Master
# 
# Certified Agile Professional
# 
# Lean Six Sigma Master Black Belt 
# 
# PL-300 Microsoft Power Bi Data Analyst Certification
# 
# SHRM-CP Society for Human Resource Management – Senior Certified Professional
# 
# PMI-DASSM Disciplined Agile Senior Scrum Master
# 
# Certified Agile Professional
# 
# Lean Six Sigma Master Black Belt 
# 
# PL-300 Microsoft Power Bi Data Analyst Certification
# 
# Complete list of certifications found here: https://bit.ly/3lM8tXK
# 

# %% [markdown]
# ### *Certification Tracker Link*

# %%
import pandas as pd
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
df = pd.read_csv('https://raw.githubusercontent.com/Cbhami/Coraline/master/ResumeProjects/Certification%20Tracker%20Public.csv')
df.fillna(0)
df = df.rename(columns=lambda x: x.strip())
df = pd.DataFrame(df)
df1 = df.iloc[0:37, :]
df1['FINISH DATE'] = pd.to_datetime(df['FINISH DATE'])
#df1.dropna(inplace=True)
#df1 = df1.astype(str) #convert back to string format to remove date.time and just keep the date
df1.sort_values(by='FINISH DATE', inplace = True, ascending=False)
df1.dropna(subset=['FINISH DATE', 'FINISH DATE'], inplace=True)
df1.head()

# %%
Certlist = [] #create my empty list
Certdate = [] #create my empty list
Certcount = []
for a in df1['My Certifications']:
  Certlist.append(a)
for b in df1['FINISH DATE']:
  Certdate.append(b)
for c in df1['Concentration']:
  Certcount.append(c)

Cert_dict = dict(zip(Certlist, Certdate)) #Here is my dictionary of certifications
#print(Cert_dict)
Cert_dict.get('PMI-DASSM')

# %%
con_dict = df1['Concentration'].to_dict()
print(con_dict)

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
fig = plt.figure(figsize=(10, 5))
plt.hist(df1['Concentration'], width = 0.4)
plt.xticks(rotation = 45)
plt.xlabel("Concentration")
plt.ylabel("Count")
plt.title("Count by Concentration")

# %%
import numpy as np
import matplotlib.pyplot as plt
data = df1['Organization']
cost = df1['Exam & Training Cost']
fig = plt.figure(figsize = (10, 5))
plt.bar(data, cost, color ='maroon',
        width = 0.4)
plt.xlabel("Organization")
plt.ylabel("Cost")
plt.title("Cost by Organization")
plt.tick_params(axis='x', rotation=45)
plt.show()

# %%
#%pip install plotly
import plotly.express as px

fig = px.bar(
    x = df1['Skill 1'],
    labels=dict(
    x="Skill",
    y="Count")
)
fig.update_xaxes(type='category')
fig.show()

# %%
df2 = pd.DataFrame(df1)
df2.to_csv('df2.csv')


