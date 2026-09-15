from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'dalsingsarai', 'state': 'bihar', 'pin': '848114'}

address = Address(**address_dict)

patient_dict = {'name':'madhav','gender': 'male','age': 19, 'address': address}

patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump(include={'name', 'gender'}) # type: ignore

print(temp1)
print(type(temp1))

temp2 = patient1.model_dump(exclude={'address': {'state'}}) # type: ignore

print(temp2)