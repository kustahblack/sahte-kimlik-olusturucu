import random
from datetime import date, timedelta
def createRandomID():
	with open("professionLibrary.txt","r",encoding="utf-8") as file:
    		professions = file.readlines()
	professionList = [profession.strip() for profession in professions]
	selectedProfession = random.choice(professionList)

	with open("nameLibrary.txt","r",encoding="utf-8") as file:
    		names = file.readlines()
	nameList = [name.strip() for name in names]
	selectedName = random.choice(nameList)

	with open("surnameLibrary.txt","r",encoding="utf-8") as file:
 	   surnames = file.readlines()
	surnameList = [surname.strip() for surname in surnames]
	selectedSurname = random.choice(surnameList)


	with open("cityLibrary.txt","r",encoding="utf-8") as file:
  	  cities = file.readlines()
	cityList = [city.strip() for city in cities]
	selectedCity = random.choice(cityList)
	
	random_number = str(random.randint(1000000000, 9999999998)) + str(random.choice([0, 2, 4, 6, 8]))
	start_date = date.today().replace(year=date.today().year - 100)
	end_date = date.today()
	random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))	
	with open("database.txt", "a") as f:
    		f.write(f"AD SOYAD: {selectedName} {selectedSurname}\nMEMLEKET: {selectedCity}\nMESLEK: {selectedProfession}\nDOĞUM TARİHİ: {random_date}\nTCKN: {random_number}\n\n")

val = int(input("Şu kadar kişi için kimlik oluştur : "))
for i in range(val):
  createRandomID()

