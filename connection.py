from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials

# Replace with your downloaded JSON key file path
credentials_file = 'credentials.json'

# Define the scopes required by your application
scopes = ['https://www.googleapis.com/auth/spreadsheets']

# Use the downloaded credentials to authenticate
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scopes)
http = credentials.authorize(Http())

# Build the Sheets API service object
service = build('sheets', 'v4', http=http)

