import csv
from application import Application, Status
from datetime import date
from pathlib import Path

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
    path = Path('data.csv')
    if not path.exists():
        return []

    applications = []
    with open(path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            applications.append(Application(
                name=row['Stellenname'],
                company=row['Firma'],
                applied_at=row['Beworben am'],
                status=row['Status'],
                link=row['Link'] or None,
                notes=row['Notizen'] or None,
                id=row['ID'],
            ))
    return applications