import sqlite3
import time

contact = sqlite3.connect("facebook_Database.db")

index = contact.cursor()

def enter_tables():
	index.execute("CREATE TABLE IF NOT EXISTS facebook_Database (Name Text,Surname Text,Username Text,Password Text,Signing_time Text,Age Text) ")
	contact.commit()
enter_tables()

def add_info(name,surname,user,passwd,signing_time,age):
	index.execute("INSERT INTO facebook_Database VALUES(?,?,?,?,?,?)",(name,surname,user,passwd,signing_time,age))
	contact.commit()

def getallusers_infos():
	index.execute("SELECT * FROM facebook_Database")
	info = index.fetchall()
	print("Loading...")
	time.sleep(2)
	for i in info:
		print(*i)

def get_oneuserinfos():
	index.execute("SELECT * FROM facebook_Database WHERE Username=?", (input("Qaysi User'ning Ma'lumotlari kerak?: "),))
	info = index.fetchall()
	print("Loading...")
	time.sleep(2)
	for i in info:
		print(*i)

def update_user():
	index.execute("UPDATE facebook_Database SET Username = ? WHERE Username=?",(input("Qanday Username'ga: "),input("Qaysi Username'ni o'zgartirmoqchisiz: "),))
	contact.commit()

def update_name():
	index.execute("UPDATE facebook_Database SET Name = ? WHERE Username=?",(input("Qanday Ismga: "),input("Qaysi User'ni o'zgartirmoqchisiz?: "),))
	contact.commit()

def update_surname():
	index.execute("UPDATE facebook_Database SET Surname = ? WHERE Username=?",(input("Qanday Familiyaga: "),input("Qaysi User'ni o'zgartirmoqchisiz?: "),))
	contact.commit()

def update_passwd():
	index.execute("UPDATE facebook_Database SET Password = ? WHERE Username=?",(input("Qaysi Passwordga: "),input("Qaysi User'ni o'zgartirmoqchisiz?: "),))
	contact.commit()

def update_signin():
	index.execute("UPDATE facebook_Database SET Signing_time = ? WHERE Username=?",(input("Qanday Vaqtga: "),input("Qaysi User'ni o'zgartirmoqchisiz?: "),))
	contact.commit()

def update_age():
	index.execute("UPDATE facebook_Database SET Age = ? WHERE Username=?",(input("Nechi Yoshga: "),input("Qaysi User'ni o'zgartirmoqchisiz?: "),))
	contact.commit()

def writeinfos_tofile():
	index.execute("SELECT * FROM facebook_Database")
	info = index.fetchall()
	with open("alluser_infos.txt","a") as face:
		for i in info:
			string = str(i)
			face.write(string)
			face.write("\n")

def write_only1user():
	index.execute("SELECT * FROM facebook_Database WHERE Username=?",(input("Qaysi User'ning ma'lumotini yozdirmoqchsiz?: "),))
	info = index.fetchall()
	with open("oneuser_infos.txt","a") as face:
		for i in info:
			string = str(i)
			face.write(string)
			face.write("\n")

def delete_one():
	index.execute("DELETE FROM facebook_Database WHERE Username = ?",(input("Qaysi User'ni tizimdan chiqarmoqchisiz?: "),))
	contact.commit()

def delete_all():
	index.execute("DELETE FROM facebook_Database")
	contact.commit()

def menyu():
	print("""
|------------------------  MENYU  ------------------------|		
|1. Foydalanuvchi[user] ma'lumotlarini kiritish.      
|2. Hamma foydalanuvchining ma'lumotlarini ko'rish.   
|3. Faqat bitta foydalanuvchining ma'lumotini ko'rish.
|4. Ma'lumotlarni yangilash.
|5. Barcha foydalanuvchining ma'lumotlarini faylga yozdirish.
|6. Tanlangan foydalanuvchining ma'lumotlarini faylga yozdirish.
|7. Bitta foydalanuvchini o'chirish. 					 
|8. Hamma foydalanuvchini o'chirish.
|9. Menyuni ko'rish.
|10.Muallif haqida va
aloqa.										 
|0. Chiqish uchun.										  
|---------------------------------------------------------|
""")

def author():
	print("""|Muallif:
|Ism va sharif: Haydarov Muzaffar
|Tug'ilgan yili: 2006.17.06
|Telefon raqami: +998889008817
|E-mail: muzaffarhaydarov77@gmail.com
""")

while True:
	choose = int(input("""
			|<\- Facebook Database -/>|
			| Xush kelibsiz, Xo'jayin!|
			|       MENYU Paneli      |

			1. Foydalanuvchi[user] ma'lumotlarini kiritish;
			2. Hamma foydalanuvchining ma'lumotlarini ko'rish;
			3. Faqat bitta foydalanuvchining ma'lumotini ko'rish;
			4. Ma'lumotlarni yangilash;
			5. Barcha foydalanuvchining ma'lumotlarini faylga yozdirish;
			6. Tanlangan foydalanuvchining ma'lumotlarini faylga yozdirish;
			7. Bitta foydalanuvchini o'chirish;
			8. Hamma foydalanuvchini o'chirish;
			9. Menyuni ko'rish;
			0. Chiqish uchun!

			Tanglang: """))

	if choose == 1:
		name = input("Ismni kiriting: ")
		surname = input("Familiyani kiriting: ")
		user = input("Usernameni kiriting: ")
		passwd = input("Parolni kiriting: ")
		signing_time = input("Ro'yhatdan o'tgan vaqtingizni kiriting: ")
		age = input("Yoshni kiriting: ")
		print("Ma'lumotlar muvaffaqiyalti qo'shildi!")
		add_info(name,surname,user,passwd,signing_time,age)
	elif choose == 2:
		getallusers_infos()
	elif choose == 3:
		get_oneuserinfos()
	elif choose == 4:
		tanlov = int(input("""
		|<-Ma'lumotlarni yangilash bo'limi->|
				~ Xush kelibsiz ~				
1. Username'ni o'zgartirish;
2. Ismni yangilash;
3. Familiyani yangilash;
4. Parolni yangilash;
5. Ro'yhatdan o'tgan vaqtni yangilash;
6. Yoshni yangilash.
Tanglang: """))
		if tanlov == 1:
			update_user()
			print("Username yangilandi!")
		elif tanlov == 2:
			update_name()
			print("Ism yangilandi!")
		elif tanlov == 3:
			update_surname()
			print("Familiya yangilandi!")
		elif tanlov == 4:
			update_passwd()
			print("Parol yangilandi!")
		elif tanlov == 5:
			update_signin()
			print("Ro'yxatdan o'tgan vaqtingiz yangilandi!")
		elif tanlov == 6:
			update_age()
			print("Yosh yangilandi!")

	elif choose == 5:
		writeinfos_tofile()
		print("Barcha foydalanuvchilar faylga yozdirildi!")
	elif choose == 6:
		write_only1user()
		print("Tanlangan foydalanuvchining ma'lumotlari faylga yozdirildi!")
	elif choose == 7:
		delete_one()
		print("O'chirildi!")
	elif choose == 8:
		delete_all()
		print("Hammasi o'chirildi!")
	elif choose == 9:
		menyu()
		print("Menyu ekranga chiqarildi!")
	elif choose == 10:
		author()
	elif choose == 0:
		print("Hayr, salomat bo'ling!!!")
		break
	else:
		print("0-9 gacha qiymat kiriting!")

contact.close()
