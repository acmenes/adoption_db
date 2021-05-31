"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

# CREATE SOME PETS

pet1 = Pet(name="Ernest Hemmingway", 
species="cat", photo_url="https://cataas.com/cat/6028590ffdeef60017d4a930", 
age=0, notes="Ernest is very smol and love naps. He also loves reading. His ideal day is cozying up on the couch with a good book. Will you give him his furever home? Fun fact, like all Hemmingway cats, Ernest has extra toes!", 
available=1)

pet2 = Pet(name="Tortelini", 
species="cat", photo_url="https://cataas.com/cat/6051d46751c45a00170727b5",
age=1, notes="Tortelini is a gorgeous tortie girl who is an absolute sweetie! She loves lazing on the couch and scritches behind her ear. Her favorite food is salmon. She's also soooo soft to the touch and has lots of love to give!", 
available=1)

pet3 = Pet(name="Xena, Warrior Kitty", 
species="cat", photo_url="https://cataas.com/cat/6011ea800a1a700011a6fae2",
age=1, notes="Wow! Talk about a little huntress! This beautiful calico kitty loves hunting mice. Perfect for apartments in NYC where the mice take over. Xena is affectionate but also independent. She also loves exercise and chasing toys!", 
available=1)

pet4 = Pet(name="Amelia", species="cat", photo_url ="https://cataas.com/cat/60b214cfee9e4c0017545639", 
age=10, notes="This purrfect creamsicle girl loves playing with her toys, eating SNAX and screaming incessantly. Her favorite time of day is 5AM which is her crazy time- she loves to zoom back and forth and sing operatic arias. Obsessed with birds, screaming. Also, she LOVES belly rubs!", available=0)

db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()

