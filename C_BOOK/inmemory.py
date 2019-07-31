from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list = []
    @classmethod
    def addContact(cls):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        mobile = input("Enter the mobile: ")
        address = input("Enter the address: ")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"Contact is added successfully with name {name}")

    @classmethod
    def deleteContact(cls):
        name = input("enter the name to be deleted:")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"Contact {name} is deleted successfully...")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"Contact with name : {name} is not found...")

    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)

    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0:
            name = input("enter the name to search:")
            s_list = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))
            if(len(s_list)) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"There is no data found with the given string")

        else:
            print("contact book is empty!...you cant do search...")


    @classmethod
    def updateContact(cls):
        name = input("enter the name to update")
        contact = cls.get_contact_by_name(name)
        if contact:
            print("1 Name 2.email 3.mobile 4.address")
            ch = int(input("enter your cjhoice"))
            if ch == 1:
                print(f"Old name : {contact.get__name()}")
                name = input("enter the new name")
                if name:
                    contact.set__name(name)
            elif ch == 2:
                print(f"Old email : {contact.get__email()}")
                email = input("enter the new email")
                if email:
                    contact.set__email(email)
            elif ch == 3:
                print(f"Old mobile : {contact.get__mobile()}")
                mobile = input("enter the new mobile")
                if mobile:
                    contact.set__mobile(mobile)
            elif ch == 4:
                print(f"Old address : {contact.get__address()}")
                address = input("enter the new address")
                if address:
                    contact.set__address(address)
        else:
            print(f"contact is not found wit the given name: {name}")

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ["Name", "Email","Mobile","Adress"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"Contact Book is empty!...")

    @classmethod
    def get_contact_by_name(cls,name):
         if len(cls.contact_list) > 0:
             contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
             return contact[0] if contact else None

        
