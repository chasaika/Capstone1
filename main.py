import datetime as dt

#==============================================================================================================
# DATABASE PATIENTS
PATIENTS = [
    {
        "id": 1,
        "name": "Ariana Grande",
        "address": "Jalan Dukuh II No.44, Bandung",
        "birth_location": "Bogor",
        "birth_date": "26-06-1993",
        "gender": "female",
        "marital_status": "single",
        "medical_records": [
            {
                "id": 1,
                "date": "14-10-2022",
                "diagnosis": "Gangguan pita suara"
            },
            {
                "id": 2,
                "date": "12-10-2022",
                "diagnosis": "Sinusitis"
            },
            {
                "id": 3,
                "date": "15-06-2023",
                "diagnosis": "Gangguan lambung"
            }
        ]
    },
    {
        "id": 2,
        "name": "John Mayer",
        "address": "Jalan Kecapi no. 64, Bandung",
        "birth_location": "Bandung",
        "birth_date": "16-10-1977",
        "gender": "male",
        "marital_status": "single",
        "medical_records": [
            {
                "id": 11,
                "date": "27-09-2022",
                "diagnosis": "Radang amandel "
            },
            {
                "id": 12,
                "date": "08-10-2022",
                "diagnosis": "Polip hidung"
            },
            {
                "id": 13,
                "date": "23-03-2023",
                "diagnosis": "Rhinitis alergi"
            },
            {
                "id": 14,
                "date": "06-05-2023",
                "diagnosis": "Laringitis"
            }
        ]
    },
    {
        "id": 3,
        "name": "Taylor Swift",
        "address": "Gg. Renner no 4",
        "birth_location": "Tangerang",
        "birth_date": "13-12-1989",
        "gender": "female",
        "marital_status": "single",
        "medical_records": [
            {
                "id": 21,
                "date": "12-05-2023",
                "diagnosis": "Konjungtivitis"
            },
            {
                "id": 22,
                "date": "26-07-2023",
                "diagnosis": "Dermatitis"
            }
        ]
    },
    {
        "id": 4,
        "name": "Katy Perry",
        "address": "Jalan Maria no 53",
        "birth_location": "Jakarta",
        "birth_date": "25-10-1984",
        "gender": "female",
        "marital_status": "married",
        "medical_records": [
            {
                "id": 31,
                "date": "30-10-2022",
                "diagnosis": "Laringitis"
            },
            {
                "id": 32,
                "date": "08-03-2023",
                "diagnosis": "Gangguan lambung"
            },
            {
                "id": 33,
                "date": "25-06-2023",
                "diagnosis": "Dermatitis atopik"
            },
            {
                "id": 34,
                "date": "23-06-2023",
                "diagnosis": "Ramsay Hunt Syndrome"
            },
            {
                "id": 35,
                "date": "03-07-2023",
                "diagnosis": "Anemia"
            }
        ]
    },
    {
        "id": 5,
        "name": "Justin Bieber",
        "address": "Jalan Dk. Argono no 1",
        "birth_location": "Sukoharjo",
        "birth_date": "01-03-1994",
        "gender": "female",
        "marital_status": "married",
        "medical_records": [
            {
                "id": 41,
                "date": "13-06-2023",
                "diagnosis": "Vertigo"
            },
            {
                "id": 42,
                "date": "15-08-2023",
                "diagnosis": "Ramsay Hunt Syndrome"
            }
        ]
    },
]

#===========================================================================================================
# MENU 1 : Add New Patient
'''
    Add patient to database

    Parameters
    ----------
    patient : dict
        Patient data
'''

def add_patient(patient: dict) -> None:
    PATIENTS.append(patient)
    return


#===========================================================================================================
# MENU 2 : Search Data Patient
    '''
    Search patient from database

    Parameters
    ----------
    search : str
        Search query 'name' or 'id'

    Returns
    -------
    dict
        Patient data
    '''

def get_patient(search: str) -> dict:
    if search.isdigit():
        for patient in PATIENTS:
            if patient['id'] == int(search):
                return patient
    else:
        for patient in PATIENTS:
            if patient['name'].lower() == search.lower():
                return patient

    return None


#===========================================================================================================
# MENU 3 : Delete Data Patient
    '''
    Delete patient from database

    Parameters
    ----------
    search : str
        Search query 'name' or 'id'
    '''

def delete_patient(patient: dict) -> None:
   
    PATIENTS.remove(patient)
    return

#===========================================================================================================
# MENU 5 : Print Data Patient
    '''
    Print patient data

    Parameters
    ----------
    patient : dict
        Patient data
    '''

def print_patient(patient: dict) -> None:
    
    print('%-20s: %s' % ('Patient ID', patient['id']))
    print('%-20s: %s' % ('Name', patient['name']))
    print('%-20s: %s' % ('Address', patient['address']))
    print('%-20s: %s' % ('Birth Location', patient['birth_location']))
    print('%-20s: %s' % ('Gender', patient['gender']))
    print('%-20s: %s' % ('Birth Date', patient['birth_date']))
    print('%-20s: %s' % ('Marital Status', patient['marital_status']))
    print('Medical Records')
    for record in patient['medical_records']:
        print('%-20s: %s' % ('Date', record['date']))
        print('%-20s: %s' % ('Diagnosis', record['diagnosis']))
    return


#===========================================================================================================
# FUNCTION MINIMIZE ERROR INPUT

def validate_name(name: str) -> bool:
    '''
    Validate name
    - Name cant be empty
    - Name at least 3 characters long
    - Name cant contain numbers
    - Name is unique
    '''
    if name == '':
        print('Name cant be empty')
        return False

    if len(name) < 3:
        print('Name at least 3 characters long')
        return False

    for char in name:
        if char.isdigit():
            print("Name can't contain numbers")
            return False

    if get_patient(name) is not None:
        print('Name must be unique')
        return False

    return True


def validate_address(address: str) -> bool:
    '''
    Validate address
    - Address cant be empty
    - Address at least 3 characters long
    '''
    if address == '':
        print("Address can't be empty")
        return False

    if len(address) < 3:
        print('Address at least 3 characters long')
        return False

    return True


def validate_birthdate(birthdate: str) -> bool:
    '''
    Validate birthdate
    - Birthdate cant be empty
    - Birthdate at least 3 characters long
    - Birthdate must be in format dd-mm-yyyy
    - Birthdate must be valid date
    '''
    if birthdate == '':
        print('Birthdate cant be empty')
        return False

    if len(birthdate) != 10:
        print('Birthdate must be in format dd-mm-yyyy')
        return False

    try:
        dt.datetime.strptime(birthdate, '%d-%m-%Y')
    except ValueError:
        print('Birthdate must be valid date')
        return False

    return True


def validate_marital_status(marital_status: str) -> bool:
    '''
    Validate marital status
    - Marital status cant be empty
    - Marital status only can be 'single', 'married', or 'divorced'
    '''
    if marital_status == '':
        print('Marital status cant be empty')
        return False

    if marital_status not in ['single', 'married', 'divorced']:
        print('Marital status only can be \'single\', \'married\', or \'divorced\'')
        return False

    return True

def validate_gender(gender: str) -> bool:
    '''
    Validate marital status
    - Marital status cant be empty
    - Marital status only can be 'single', 'married', or 'divorced'
    '''
    if gender == '':
        print('Gender cant be empty')
        return False

    if gender not in ['male', 'female']:
        print('Gender only can be \'male\', \'female\'')
        return False

    return True

#================================================================================================================

def create_patient() -> dict:
    '''
    Create patient data

    Returns
    -------
    dict
        Patient data
    '''
    patient = {
        'id': PATIENTS[-1]['id'] + 1 if len(PATIENTS) > 0 else 1,
        'name': '',
        'address': '',
        'birth_location': '',
        'birth_date': '',
        'gender': '',
        'marital_status': '',
        'medical_records': []
    }

    # validate name
    while True:
        patient['name'] = input('%-20s: ' % 'Name')
        if validate_name(patient['name']):
            break

    # validate address
    while True:
        patient['address'] = input('%-20s: ' % 'Address')
        if validate_address(patient['address']):
            break

    # validate birth location
    while True:
        patient['birth_location'] = input('%-20s: ' % 'Birth Location')
        if validate_address(patient['birth_location']):
            break

    # validate birth date
    while True:
        patient['birth_date'] = input('%-20s: ' % 'Birth Date')
        if validate_birthdate(patient['birth_date']):
            break
    
    # validate gender
    while True:
        patient['gender'] = input('%-20s: ' % 'Gender')
        if validate_gender(patient['gender']):
            break

    # validate marital status
    while True:
        patient['marital_status'] = input('%-20s: ' % 'Marital Status')
        if validate_marital_status(patient['marital_status']):
            break

    return patient

#================================================================================================================

def main() -> None:
    '''
    Main function of Hospital Management System
    '''
    while True:
        #header
        print("="*50)
        print(f"SUMBER SEHAT HOSPITAL".center(50))
        print(f"Hospital Management System".center(50))
        print("="*50)

        print('1. Add Patient')
        print('2. Search Patient')
        print('3. Delete Patient')
        print('4. Add Medical Record')
        print('5. Print All Patient')
        print('6. Exit')

        choice = input('Choice: ')

        # print new line
        print()

        if choice == '1':
            print('Add Patient')

            # create patient
            patient = create_patient()

            # find pasien if exist
            add_patient(patient)
            print('Patient added successfully')

        elif choice == '2':
            print('Search Patient')

            # search patient
            patient = get_patient(input('%-20s: ' % 'Name or ID'))

            # print patient
            if patient is not None:
                print_patient(patient)
            else:
                print('Patient not found')

        elif choice == '3':
            print('Delete Patient')

            # search patient
            patient = get_patient(input('%-20s: ' % 'Name or ID'))

            # delete patient
            if patient is not None:
                delete_patient(patient)
                print('Patient deleted successfully')
            else:
                print('Patient not found')

        elif choice == '4':
            print('Add Medical Record')

            # search patient
            patient = get_patient(input('%-20s: ' % 'Name or ID'))

            # add medical record
            if patient is not None:
                record = {
                    'id': patient['medical_records'][-1]['id'] + 1 if len(patient['medical_records']) > 0 else 1,
                    'date': dt.datetime.now().strftime('%d-%m-%Y'),
                    'diagnosis': input('%-20s: ' % 'Diagnosis')
                }
                patient['medical_records'].append(record)
                print('Medical record added successfully')
            else:
                print('Patient not found')

        elif choice == '5':
            print("="*50)
            print(f"DATABASE PATIENT SUMBER SEHAT HOSPITAL".center(50))
            print("="*50)

            # print all patient
            for patient in PATIENTS:
                print_patient(patient)
                print("-"*50)
                print()

        elif choice == '6':
            break

        else:
            print('Invalid choice')

        # print new line
        print()


if __name__ == '__main__':
    main()
