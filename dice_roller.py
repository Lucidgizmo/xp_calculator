from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import gspread

print()

# Creating Google Sheets Scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'sheet_keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1QngEdhD8Bp_uVBXKeorX_LZItTOva_rgvYidkexwGEw'
gsheet = SAMPLE_SPREADSHEET_ID



# Create service and call it
# Get Caster Level.
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="diceroller!A1:Ui6").execute()
values = result.get('values', [])
print(values)





# dice rolling app
import random

def Roll_Stats_3d6():
    numberOfStats = 6
    for i in range(numberOfStats):
        Roll_1 =(random.randint(1, 6))
        Roll_2 =(random.randint(1, 6))
        Roll_3 =(random.randint(1, 6))
        Total = Roll_1 + Roll_2 + Roll_3
        print("You rolled a " + str(Total))



def Roll_Custom_Dice():
    numberOfDice = int(input("How many dice do you want to roll? "))
    numberOfSides = int(input("How many sides should each die have? "))
    for i in range(numberOfDice):
        (print("You rolled a" + int(random.randint(1, numberOfSides))))

def Roll_Caster_Lvl_D6():
    numberOfDice = 6 # This will end up taking the caster level from the sheet.
    total_of_rolls = 0
    for i in range(numberOfDice):
        Roll = (random.randint(1, 6))
        print(Roll, end=" ")
        total_of_rolls += Roll
    print("\n" + "Your total rolls add up to " + str(total_of_rolls))




def Roll_4d6_Droplowest():
    numberOfStats = 6
    for i in range(numberOfStats):
        rolls = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        #print(rolls)
        rolls.remove(min(rolls))
        total = sum(rolls) #adds rolls together, just declaring sum(rolls), then printing rolls fails
        print(total)
# List of Dice Rolling Functions - Implemented

# Roll_Custom_Dice()   Roll_Stats_3d6()   Roll_4d6_Droplowest()
# Roll_Caster_Lvl_D6()

# List of Dice Rolling Functions - Not yet implemented
# Roll_Caster_Lvl_D8()   Roll_Caster_Lvl_D10()   Roll_Caster_Lvl_D12()   Roll_Caster_Lvl_D20()
# Roll_Caster_Lvl_D4()