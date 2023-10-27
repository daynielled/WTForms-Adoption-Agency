from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Woofly = Pet(name= 'Woofly', species='dog',photo_url='https://thumbs.dreamstime.com/b/cute-dog-26621836.jpg', age='3')
Porchetta = Pet(name='Porchetta', species='porcupine', photo_url= 'https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg',age= '2')
Snargle = Pet(name='Snargle', species='cat', photo_url= 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Black-Tailed_Prairie_Dog.jpg',age= '1')

db.session.add(Woofly)
db.session.add(Porchetta)
db.session.add(Snargle)

db.session.commit()

