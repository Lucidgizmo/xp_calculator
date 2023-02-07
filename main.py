from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import gspread

# Creating Google Sheets Scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'sheet_keys.json'

credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1QngEdhD8Bp_uVBXKeorX_LZItTOva_rgvYidkexwGEw'
gsheet = SAMPLE_SPREADSHEET_ID

party_size = int(input("What is the number of party members? "))
party_level = int(input("What is the party's level? "))
encounter_level = int(input("What is the encounter level "))

# Create service and call it
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="xptable!A1:U22").execute()
values = result.get('values', [])
#for row in values:
    #print(row)
cell_value = result["values"][encounter_level+1][party_level]
xp_per_member = int(cell_value) / int(party_size)
print("The party has earned " + str(cell_value) + " points of experience")
print("Each party member gets " + str(xp_per_member) + " points of experience")






