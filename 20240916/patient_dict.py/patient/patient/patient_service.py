from Patient import Patient
#patient = Patient(100,'Rohit')
#print(patient)
#2. patients{}
patients = {} #dict()


# Function to add a patient
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id] = patient #patients.append(patient)
    print('Patient created successfully')
    

# Function to remove a patient
def patient_remove(id):
    global patients
    patient = patients.get(id)
   # for patient in patients:
    if patient == None:
        print(f'No such id {id}') 
        return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        del patients[id] #patients.remove(patient)
        print('Patient deleted successfully')

         
def patient_display():
    global patients
    for id in patients: #for patient in patients: 
        print(patients[id]) #print(patient)

def patient_display_byid(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return 
    print(patient)  


def patient_update(id):
    global patients
    patient = patients.get(id)
    if patient == None: 
        print(f'No such id {id}')
        return
    print(patient)
    name = input(f'Enter new name({patient.name}):')
    patient.name = name
    print('Patient updated successfully')