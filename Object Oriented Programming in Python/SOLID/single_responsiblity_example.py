# class Person:
#     """
#     Person class with two jobs:
#     - Manage the Person's proptery
#     - Store the person in the db
#     """
#     def __init__(self, name):
#         self.name = name
        
#     def __repr__(self):
#         return f"Person(name={self.name})"
    
#     @classmethod
#     def save(cls, person):
#         print(f"Save the {person} to the database")
        
    
class PersonDB:
    """
    PersonDB class with only one job:
    - Store the person in the db
    """
    def save(self, person):
        print(f"Save the {person} to the database")
        
class Person:
    """
    Person class with only one job:
    - Manage the Person's proptery
    """
    def __init__(self, name):
        self.name = name
        self.db = PersonDB()
        
    def __repr__(self):
        return f"Person(name={self.name})"
    
if __name__ == "__main__":
    p = Person('John Doe')
    p.db.save(p)