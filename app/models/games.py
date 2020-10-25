import pymongo
from bson.objectid import ObjectId

class Games:
    def __init__(self, id=None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["gamecenterku"]
        self.col_games = db["games"]
        if id:
            self.id = ObjectId(id)
    
    def getId(self):
        return self.id
    
    def getUserId(self):
        get = self.col_games.find_one({"_id":self.id}, {"user_id" : 1})
        if get == None:
            return None
        return get['user_id']
    
    def setUserId(self, user_id):
        new = { "$set": { "user_id": user_id } }
        return self.col_games.update_one({"_id":self.id}, new)
    
    def getGamename(self):
        get = self.col_games.find_one({"_id":self.id}, {"game_name" : 1})
        if get == None:
            return None
        return get['game_name']
    
    def setTitle(self, game_name):
        new = { "$set": { "game_name": game_name } }
        return self.col_games.update_one({"_id":self.id}, new)
    
    def getDev(self):
        get = self.col_games.find_one({"_id":self.id}, {"dev" : 1})
        if get == None:
            return None
        return get['dev']
    
    def setDev(self, dev):
        new = { "$set": { "dev": dev } }
        return self.col_games.update_one({"_id":self.id}, new)

    def getImage(self):
        get = self.col_games.find_one({"_id":self.id}, {"image" : 1})
        if get == None:
            return None
        return get['image']
    
    def setImage(self, image):
        new = { "$set": { "image": image } }
        return self.col_games.update_one({"_id":self.id}, new)

    def getItem(self):
        get = self.col_games.find_one({"_id":self.id}, {"item" : 1})
        if get == None:
            return None
        return get['item']
    
    def setItem(self, item):
        new = { "$set": { "item": item } }
        return self.col_games.update_one({"_id":self.id}, new)

    def showAllGame(self):
        arr = []
        for x in self.col_games.find():
            arr.append(x)
        return arr
    
    def getData(self):
        return self.col_games.find_one({"_id":self.id})
    
    def addGame(self, user_id, game_name, dev, image, item):
        dict_games = {"user_id":user_id, "game_name":game_name, "dev":dev, "image":image, "item":item}
        insert = self.col_games.insert_one(dict_games)
        idgames = insert.inserted_id
        return idgames
    
    def deleteGame(self):
        query = { "_id": self.id }
        return self.col_games.delete_one(query)
