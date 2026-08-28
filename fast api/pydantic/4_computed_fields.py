from pydantic import BaseModel,EmailStr, computed_field
from typing import List,Dict

class Patient(BaseModel):

    name : str
    age : int
    email: EmailStr
    weight : float
    height : float
    married: bool
    allergies : List[str]
    contact_details: Dict[str,str]
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print('bmi', patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {'name': 'nitish', 'age': 90, "email": "abc@gmail.com", 'weight': 75.43,'height': 1.71, 'married': True, "allergies": ["nuts", "honey"], "contact_details": { "phone": "99391144555"}}

patient = Patient(**patient_info)


update_patient_data(patient)