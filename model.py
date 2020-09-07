import uuid
import json
from db import DataBase

database = DataBase('db.json')



class Member:
    def __init__(self, name, proficiency_level, age, dept, zindi=None, kaggle=None):
        self.id = uuid.uuid1().hex
        self.name = name
        self.proficiency_level = proficiency_level
        self.age = age
        self.dept = dept
        self.zindi = zindi
        self.kaggle = kaggle

    @staticmethod
    def Lead():
        twitter = 'https://twitter.com/mofeloluwa_agba_dev'
        name = 'Mofeloluwa Lijadu'
        return "Lijadu Obafunmilayo Mofeloluwa is a staunch Machine learning Engineer and a Student of Electrical Electronics Engineering FUTA. He is currently the DSC LEAD and he has trained many students in the AI field."
    
    def save(self):
        info = self.__dict__
        with open('db.json', 'r') as db:
            data = json.load(db)
            all_ids = [mem['id'] for mem in data['DSN-MEMBERS']]
            if self.id in all_ids:
                data['DSN-MEMBERS'][all_ids.index(self.id)] = info
            else:
                data['DSN-MEMBERS'].append(info)

        with open('db.json', 'w') as db:
            json.dump(data, db, indent=2)

    def delete(self):
        with open('db.json', 'r') as db:
            data = json.load(db)
            data['DSN-MEMBERS'] = list(filter(lambda member:member['id']!=self.id, data['DSN-MEMBERS']))
        
        with open('db.json', 'w') as db:
            json.dump(data, db, indent=2)

    @staticmethod
    def retrieve(id):
        with open('db.json', 'r') as db:
            data = json.load(db)
            info = list(filter(lambda member: member['id']==id, data['DSN-MEMBERS']))
        return info[0]
