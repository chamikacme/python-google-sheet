from connection import service

# function to get all values from the spreadsheet
def get_all_values(spreadsheet_id, range):
    sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range).execute()
    return sheet.get('values', [])

# response = get_all_values(spreadsheet_id, 'Sheet1!A1:B2')
# print(response)

# function to get all sheets from the spreadsheet
def get_all_sheets(spreadsheet_id):
    sheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return sheet.get('sheets', [])

# response = get_all_sheets(spreadsheet_id)
# print(response)

# function to write values to the spreadsheet
def write_values(spreadsheet_id, range, values):
    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range, valueInputOption='RAW', body=body).execute()
    return result

# response = write_values(spreadsheet_id, 'Sheet1!A1:B2', [['Hello', 'World']])
# print(response)

# function to create a new sheet in the spreadsheet
def create_sheet(spreadsheet_id, title):
    body = {
        'requests': [
            {
                'addSheet': {
                    'properties': {
                        'title': title
                    }
                }
            }
        ]
    }
    result = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
    return result

# response = create_sheet(spreadsheet_id, 'Sheet2')
# print(response)

# function to delete a sheet from the spreadsheet
def delete_sheet(spreadsheet_id, sheet_id):
    body = {
        'requests': [
            {
                'deleteSheet': {
                    'sheetId': sheet_id
                }
            }
        ]
    }
    result = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
    return result

# response = delete_sheet(spreadsheet_id, 1737049857)
# print(response)

# function to add a new row to the spreadsheet
def add_row(spreadsheet_id, range, values):
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range, valueInputOption='RAW', body=body).execute()
    return result

# response = add_row(spreadsheet_id, 'Sheet1!A1:B1', [['Hello', 'World']])
# print(response)

# clear values from the spreadsheet
def clear_values(spreadsheet_id, range):
    result = service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=range).execute()
    return result

# response = clear_values(spreadsheet_id, 'Sheet1!A1:B1')
# print(response)