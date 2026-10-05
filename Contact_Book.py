import json,os
if(os.path.exists("contact_book.json")):
  with open ("contact_book.json","r") as f:
    book=json.load(f)
else:
  book={}

def valid_input(ph):
  while(len(str(ph))!=10):
    ph=get_int_input("Invalid phone number entered! Enter again (-1 to return to main menu): ")
    if ph==-1:
      return 0
  return ph

def get_int_input(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Invalid input! Please enter a number.")

def add_member():
  name=input("Enter name: ").lower()
  if name in book:
    print("Person is already present!\nDo you want to update the phone number (Yes/No)?")
    yn=input()
    if(yn.lower()=='yes'):
      update_member(name)
      return
    elif(yn.lower()=='no'):
      print("Redirecting to Main Menu...")
      return
    else:
      print("No option other than Yes,No. If you want to update a contact, select 5 from menu!")
      return
  ph=get_int_input("Enter phone number: ")
  ph=valid_input(ph)
  if(ph==0):
    return
  book[name]=[ph]
  print("Member added successfully")

def del_member():
  ch1=get_int_input("Delete:\n1. Delete a contact member\n2. Delete phone number of a contact\n3. Delete all contacts\nEnter the option: ")
  if(ch1==1):
    name=input("Enter contact name to be deleted: ").lower()
    if name in book:
      del(book[name])
      print("Contact info deleted")
      return
    print("Name not found.")
  elif ch1==2:
    name=input("Enter name whose phone number needs to be deleted: ").lower()
    if name in book:
      phone_list=book[name]
      print("Contact numbers:",phone_list)
      ph=get_int_input("Enter which phone number to be deleted: ")
      ph=valid_input(ph)
      if(ph==0):
        return
      if ph not in phone_list:
        print("Invalid Phone number. Nothing is deleted. Redirecting to main menu")
      else:
        for idx,p in enumerate(phone_list,start=0):
          if p==ph:
            phone_list.pop(idx)
        print("Number deleted successfully")
    else:
      print("Name not found")
  elif ch1==3:
    book.clear()
    print("All contacts are deleted!")
  else:
    print("Invalid choice, redirecting to main menu.")

def search_member():
  name=input("Enter name to be searched: ").lower()
  if name not in book:
    print("Name not found.")
    return
  print("Name:",name,"\tContact info:",book[name])

def display():
  for i in book:
      phone_list=book[i]
      print("Name:",i,"\tContact info:",phone_list)

def update_member(name):
  ch1=get_int_input("Update:\n1. Add a new number\n2. Edit a previous number\nEnter your option: ")
  if ch1==1:
    ph=get_int_input("Enter new phone number: ")
    ph=valid_input(ph)
    if(ph==0):
      return
    book[name].append(ph)
    print("Phone number updated successfully")
  elif ch1==2:
    print("Contact numbers:",book[name])
    old_ph=get_int_input("Enter the phone number to be edited: ")
    old_ph=valid_input(old_ph)
    if old_ph==0:
      return
    if old_ph not in book[name]:
      print("Invalid phone number. Nothing is edited. Redirecting to main menu")
      return
    ph=get_int_input("Enter new phone number: ")
    ph=valid_input(ph)
    if(ph==0):
      return
    for idx,p in enumerate(book[name],start=0):
        if p==old_ph:
          book[name][idx]=ph
    print("Phone number edited successfully")
  else:
    print("Invalid choice, redirecting to main menu.")
ch=1
print("CONTACT BOOK")
while(ch!=6):
  ch=get_int_input("\nMENU:\n1. Add a new member\n2. Delete a member\n3. Search for a member\n4. Display the contact book\n5. Update a contact\n6. Exit\nEnter your choice:")
  match(ch):
    case 1:
      add_member()
      with open ("contact_book.json","w") as f:
        json.dump(book,f)
    case 2:
      if book=={}:
        print("Contact list is empty.")
        continue
      del_member()
      with open ("contact_book.json","w") as f:
        json.dump(book,f)
    case 3:
      if book=={}:
        print("Contact list is empty.")
        continue
      search_member()
    case 4:
      if book=={}:
        print("Contact list is empty.")
        continue
      display()
    case 5:
      if book=={}:
        print("Contact list is empty.")
        continue
      display()
      name=input("\nEnter name to update the contact number: ").lower()
      if name not in book:
        print("Name not found")
        continue
      update_member(name)
      with open ("contact_book.json","w") as f:
        json.dump(book,f)
    case 6:
      break
    case _:
      print("Invalid choice")