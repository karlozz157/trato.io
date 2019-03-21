from prexto_trato import Contract

"""
Ver documentación para ver las opciones de configuración tanto variables como participantes
https://enterprise.app.trato.io/api/docs
"""

contract = Contract('5c7990130b2f730ebc3cc183')

print(contract.get_vars())
print(contract.set_vars('5c33a6037a27e3447c9586a7', {'p1_prexto': 'ejemplo'}))
print(contract.get_vars())

print(contract.get_participant('5c3e669e4843d40ce935b824'))
print(contract.set_participant('5c3e669e4843d40ce935b824', {'name': 'Dan', 'email': 'dandelgadomendoza@gmail.com', 'phone': '5539014374'}))
print(contract.get_participant('5c3e669e4843d40ce935b824'))

print(contract.to_sign()) #{"success":true}
