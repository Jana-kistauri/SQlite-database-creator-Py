
import sqlite3


class DataBase:

	def __init__(self, db_name, table_name, merged_list):
		self.db_name = db_name
		self.table_name = table_name
		self.merged_list = merged_list


	def create_db(self):
		connection = sqlite3.connect(f"{self.db_name}.db")
		cursor = connection.cursor()

		return (cursor, connection)


	def create_table(self, cursor):
		cursor.execute("""CREATE TABLE IF NOT EXISTS new_table(
							id INTEGER PRIMARY KEY AUTOINCREMENT)""")

		cursor.execute("ALTER TABLE new_table RENAME TO {}".format(self.table_name))


	def create_columns(self, cursor, connection):

		for i in range(table_columns):
			cursor.execute("ALTER TABLE {} ADD COLUMN {} {}".format(self.table_name, self.merged_list[i][0], self.merged_list[i][1]))


		connection.commit()
		cursor.close()
		connection.close()	



def checkAmountType(amount):
	while True:

		if not amount.isdigit():
			amount = input("გთხოვთ, შეიტანეთ რიცხვი: ")
			continue

		if  int(amount) < 0:
			amount = input("გთხოვთ, შეიტანეთ დადებითი რიცხვი: ")
			continue

		amount = int(amount)
		break

	return amount



def checkColumnType(item):

	while True:

		if item.isdigit():
			print("გთხოვთ, რიცხვის ნაცვლად შეიყვანეთ სწორი ტიპი!")
			item = input("TEXT, INTEGER, NUMERIC, REAL, NONE: ")
			continue
		else:
			item = item.lower()



		if not (item == "text" or item == "integer" or item == "numeric" or item == "real" or item == "none"):
			print("გთხოვთ, შეიყვანეთ ერთეულის სწორი დასახელება!")
			item = input("(TEXT, INTEGER, NUMERIC, REAL, NONE): ")
			continue

		item = item.upper()
		break

	return item


def check_spaces_in_name(item):
	item = item.replace(" ", "_")
	return item


def generate_column_names_and_types():
	for i in range(table_columns):

		column_name = input("შეიტანეთ სვეტის სახელი: ")
		column_name = check_spaces_in_name(column_name)

		column_type = input("შეიტანეთ სვეტის ტიპი: ")
		column_type = checkColumnType(column_type)

		column_names.append(column_name)
		column_types.append(column_type)



def merge(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]

    return merged_list



db_name = input("რა სახელით გსურთ ბაზის შექმნა? ")

table_name = input("შეიტანეთ ცხრილის სახელი: ")
table_name = check_spaces_in_name(table_name)

table_columns = input("შეიტანეთ ცხრილის სვეტების რაოდენობა: ")
table_columns = checkAmountType(table_columns)


column_names = []
column_types = []
generate_column_names_and_types()


merged_list = []
merged_list = merge(column_names, column_types)
	

db = DataBase(db_name, table_name, merged_list)

db.create_db()

cursor = db.create_db()[0]
connection = db.create_db()[1]

db.create_table(cursor)
db.create_columns(cursor, connection)







		