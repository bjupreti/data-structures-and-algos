# class PersonStorage:
#     """
#     PersonStorage class which has two methods
#     - The save_in_db() method saves a person to db.
#     - The save_in_json() method saves a person to a JSON file.
    
#     Later, if you want to save the Person's object into an XML file, you must modify the PersonStorage class. It means that the PersonStorage class is not open for extension but modification. Hence, it violates the open-closed principle.
#     """
#     def save_in_db(self, person):
#         print(f"Saving {person} in DB")
    
#     def save_in_json(self, person):
#         print(f"Saving {person} in JSON format")

from abc import ABC, abstractmethod
class PersonStorage(ABC):
    @abstractmethod
    def save(self):
        pass
    
class PersonDB(PersonStorage):
    def save(self, person):
        print(f"Saving {person} in db")
        
class PersonJSON(PersonStorage):
    def save(self, person):
        print(f"Saving {person} in JSON")
        
class PersonXML(PersonStorage):
    def save(self, person):
        print(f"Saving {person} in XML")
        
    
    
class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Person(name={self.name})"
    

p = Person('Bijay')
storage = PersonXML()
storage.save(p)