import csv
from application import Application, Status
from datetime import date

def save_applications(applications):
    with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Stellenname', 'Firma', 'Link', 'Beworben am', 'Status', 'Notizen', 'ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows([application_to_dictionary(app) for app in applications])

def application_to_dictionary(application: Application): 
    return {'Stellenname': application.name, 
            'Firma': application.company, 
            'Link': application.link or "", 
            'Beworben am': application.applied_at.isoformat(), 
            'Status': application.status.value, 
            'Notizen': application.notes or "", 
            'ID': application.id
    }

def load_applications(): 
    #TODO