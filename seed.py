from app import db
from models import Pet, db

db.drop_all()
db.create_all()

pet_1 = Pet(name="Spade", species="Lab", available=True)
pet_2 = Pet(name="Locke", species="Shih Tzu")
pet_3 = Pet(name="Ace", age=5, species="Rottweiler", available=False)

db.session.add(pet_1)
db.session.add(pet_2)
db.session.add(pet_3)

db.session.commit()
