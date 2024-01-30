#_________Contact Management System_________
#import necessary packages for doing this project

import datetime
import csv
import os
import re

#create function for title

def title():
	line_1 = '_________________________________'
	title = 'CONTACTS MANAGEMENT SYSTEM'
	line_2 = '_________________________________'

	print(line_1.center(130))
	print(title.center(130))
	print(line_2.center(130))

#create a class for all function options
class contact_function:
	contact_fields = ['Name','Mobile_No'] #column names
	contact_database = "contacts.csv"
	contact_data = [] # this list is used to temporary store the data

	#create function
	def create(self):
		os.system('cls')
		title()
		print('   Create Contact: ')
		print('   ----------------')
		print("")
		#now one by one iterate the contact fields

		for fields in self.contact_fields:
			contact_details = input('   Enter '+ fields + ':')
			print('')

			#write validation logic for name field
			if fields == 'Name':
				m = re.match("[a-zA-Z]",contact_details)

				if m != None:
					self.contact_data.append(contact_details)
				else:
					print('Enter a valid name.'.center(129))
					return

			#write validation logic for mobile number integer and equal to 10.
			if fields == 'Mobile_No':
				m = re.fullmatch("[7-9][0-9]{9}" ,contact_details)

				if m != None:
					self.contact_data.append(contact_details)
				else:
					print("Invalid Mobile_No,Please Enter a valid mobile number..".center(129))
					return


		#now we get data from system
		Date = datetime.datetime.today()
		d = Date.strftime("%B %d %Y") #this function is used to give the formate of the date
		self.contact_data.append(d)

		#now insert the input in csv file

		with open(self.contact_database, 'a') as file:
			write = csv.writer(file)
			write.writerows([self.contact_data])

		self.contact_data = [] #we will clear the contact data list to get more contact
		print('')
		print('Contact is Created Successfully'.center(129))
		print('')

	#view function
	def view(self):
		os.system('cls')
		title()

		print('Contacts: '.center(10))
		print('__________'.center(10))
		print('')

		count = 0

		#now open the csv file to read
		with open(self.contact_database, 'r') as file:
			read = csv.reader(file)
			for data1 in read:
				if len(data1) > 0:
					count += 1

			print('Total Contacts: ',count)
			print('')

		#display the all data
		with open(self.contact_database, 'r') as file:
			read = csv.reader(file)

			if os.path.getsize(self.contact_database) == 0:
				print('Contact book is empty, Please create Contacts.'.center(129))
			else:
				for fields in self.contact_fields:
					    print('{0:<10}'.format(fields).center(10), end = '\t\t')
				print('{0:<10}'.format("Date"))
				print('{:<10}\t\t{:<10}\t\t{:<10}'.format('----','----------','----'))
				print('')

				for data in read:
					for item in data:
						print('{:<10}'.format(item).center(10), end='\t\t')

					print('')

				print('\n')
				input('\t Press enter key to continue..'.center(120))
				os.system('cls')
				print('')


    #delete() function
	def delete(self):

		os.system('cls')
		title()

		print('Delete Contacts: '.center(10))
		print('-----------------'.center(10))
		print('')

		self.contact_match = 'false'
		delete_value = input('Enter your name: ')
		delete_value.lower()
		update_list = [] #this empty list help to update the database

    	#reading file to get match of the search
		with open(self.contact_database, 'r') as file:
			read = csv.reader(file)

			for data in read:
				if len(data) > 0:
					if delete_value != data[0].lower():
						update_list.append(data)
					else:
						self.contact_match = 'true'

    	#conditions to delete matched contact
		if self.contact_match == 'true':
			with open(self.contact_database, 'w') as file:
				write = csv.writer(file)
				write.writerows(update_list)
				print('')
				print('Contact is deleted Successfully.'.center(129))
				print('')

		if self.contact_match == 'false':
			print('')
			print('Sorry! data not found'.center(129))
			print('')


	#search() function
	def search(self):
		os.system('cls')
		title()

		print('Search Contacts: '.center(10))
		print('-----------------'.center(10))
		print('')

		self.contact_match = 'false'
		search_value = input('Enter your name: ')
		search_value.lower()
		print('')

		#first display the field names
		for fields in self.contact_fields:
			print('{0:<10}'.format(fields).center(10), end= '\t\t')

		print('{0:<10}'.format('Date'))
		print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','----------','-----'))
		print('')

		#read the database for match
		with open(self.contact_database, 'r') as file:
			read = csv.reader(file)

			for data in read:
				if len(data):
					if search_value == data[0].lower():
						self.contact_match = 'true'
						print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))

		
		if self.contact_match == 'false':
			print('')
			print('Sorry, their is no any contact available with this name..'.center(129))

		print('')

	#update() function
	def update(self):
		os.system('cls')
		title()

		print('Edit Contacts: '.center(10))
		print('-----------------'.center(10))
		print('')



		self.contact_match = 'false'
		search_value = input('Enter your name: ')
		search_value.lower()
		print('')	

		#first display the field names
		for fields in self.contact_fields:
			print('{0:<10}'.format(fields).center(10), end= '\t\t')

		print('{0:<10}'.format('Date'))
		print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','----------','-----'))
		print('')

		#read the database for match
		with open(self.contact_database, 'r+') as file:
			read = csv.reader(file)
			prev = []
			curr = []

			for data in read:
				if len(data):
					if search_value == data[0].lower():
						self.contact_match = 'true'
						print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))

						resp= int(input('What you want to Edit Name or Number?, press 1 for Name and 2 for Number.'))

						#write the logic for changing the name.
						if resp == 1:
							
							name = input('Enter your new name: ')
							data[0] = name
							curr.append(data)

						elif resp == 2:

							mob = input('Enter your new number: ')
							data[1] = mob
							curr.append(data)
						

					else:
						prev.append(data)

					with open(self.contact_database, 'w') as file:
						write = csv.writer(file)
						write.writerows(curr)
						write.writerows(prev)

								
        

		
		if self.contact_match == 'false':
			print('')
			print('Sorry, their is no any contact available with this name..'.center(129))
		else:
			print('')
			print('Your new data is Updated Successfully!'.center(129))

		print('')	



#creating object of the class
contact_class = contact_function()
		


#now using os module we will clear the console
os.system('cls')
title()

while True:
	print('1. View Contacts'.center(128))
	print('2. Create Contacts'.center(129))
	print('3. Search Contacts'.center(129))
	print('4. Update Contacts'.center(129))
	print('5. Delete Contacts'.center(129))
	print('6. Exit'.center(120))
	print('_________________________________'.center(129))
	print('')
	option = int(input('\t\t\t\t\t\t Choose your option: '))

	if option == 1:
		
		contact_class.view()
		title()

	elif option == 2:
		
		while True:
			contact_class.create()
			ans = input('\t\t\t\t\t\tDo you want to create another contact number?[Y/N]:')

			if ans == 'Y' or ans == 'y':
				continue
			else:
				break

		os.system('cls')
		title()


	elif option == 3:

		while True:
			contact_class.search()
			ans = input('\t\t\t\t\t\tDo you want to Search another contact number?[Y/N]:')

			if ans == 'Y' or ans == 'y':
				continue
			else:
				break

		os.system('cls')
		title()
		
	elif option == 4:
		
		while True:
			contact_class.update()
			ans = input('\t\t\t\t\t\tDo you want to Update another contact number?[Y/N]:')

			if ans == 'Y' or ans == 'y':
				continue
			else:
				break

		os.system('cls')
		title()	

	elif option == 5:

		while True:
			contact_class.delete()
			ans = input('\t\t\t\t\t\tDo you want to Delete another contact number?[Y/N]:')

			if ans == 'Y' or ans == 'y':
				continue
			else:
				break

		os.system('cls')
		title()

	elif option == 6:
		os.system('cls')
		break
	else:
	
		while True:
			print('Invalid Choice!'.center(129))
			ans = input('\t\t\t\t\t\tDo you want to enter another option?[Y/N]:')

			if ans == 'Y' or ans == 'y':
				flag = 1
				break
			else:
				flag = 0
				break

		if flag == 1:
		    os.system('cls')
		    title()
		else:
			os.system('cls')
			break

