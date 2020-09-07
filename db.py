import json


class DataBase:

    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        with open(self.file_name, 'r') as db:
            data = json.load(db)
            return data

    def write(self, data):
        with open(self.file_name, 'w') as db:
            json.dump(data, db, indent=2)
            return True

    def create_collection(self, collection_name):
        data = self.load()
        data['collection_name'] = []
        self.write(data)
        return True

    def remove_collection(self, collection_name):
        data = self.load()
        del data['collection_name']
        self.write(data)
