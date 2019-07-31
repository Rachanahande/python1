from contact import contact

class ContactBook:
    contacts = []

    @staticmethod
    def addContact():
        name = input("enter the name")
        email = input("enter the email")
        mobile = input("enter the mobile")
        ContactBook.contacts.append(Contact(name,email,mobile))
    
    @staticmethod
    def searchContact():
        name = input("enter the name to be searched")
        
    @staticmethod
    def deleteContact():
        name = input("enter the name to be deleted")
    
    @staticmethod
    def viewAll():
        pass

    @staticmethod
    def updateContact():
        name = input("enter the name to update")
        contact = getContact(name)
        print("1.Email 2.Name 3.Mobile")

        
    
 