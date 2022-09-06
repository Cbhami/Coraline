from gettext import install



import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

df = pd.read_csv(r"C:\Users\coleb\OneDrive\Coraline\Resources\csv data\user94403143_workout_history.csv")
#df = pd.read_csv(r"/Users/colehamilton/Library/CloudStorage/#OneDrive-Personal/Coraline/Resources/csv data/#user94403143_workout_history.csv")
df['Date Submitted'] = pd.to_datetime(df['Date Submitted'])
df['Date Submitted'] = df['Date Submitted'].dt.strftime('%Y-%m-%d')
df['Workout Date'] = pd.to_datetime(df['Workout Date'])
df['Workout Date'] = df['Workout Date'].dt.strftime('%Y-%m-%d')
df.to_csv(r'C:\Users\coleb\OneDrive\Coraline\Resources\csv data\user94403143_workout_history.csv', index=False)
#df.to_csv(r'/Users/colehamilton/Library/CloudStorage/#OneDrive-Personal/Coraline/Resources/csv data/#user94403143_workout_history.csv', index=False)   

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

#Mac
#with open(r'/Users/colehamilton/Library/CloudStorage/#OneDrive-Personal/Coraline/Resources/csv data/#user94403143_workout_history.csv', 'r') as file_obj:
# content = file_obj.read()
# client.import_csv(spreadsheet.id, data=content)

#Windows
credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\coleb\OneDrive\Important Keys\client_secret.json', scope)
#Mac
#credentials = ServiceAccountCredentials.#from_json_keyfile_name(r'/Users/colehamilton/Library/#CloudStorage/OneDrive-Personal/client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('Data_File')

#Mac
# with open(r'/Users/colehamilton/Library/CloudStorage/#OneDrive-Personal/Coraline/Resources/csv data/#user94403143_workout_history.csv', 'r') as file_obj:
#Win
with open(r'C:\Users\coleb\OneDrive\Coraline\Resources\csv data\user94403143_workout_history.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)
