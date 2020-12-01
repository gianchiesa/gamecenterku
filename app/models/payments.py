import pymongo
from bson.objectid import ObjectId

class Payments:
    def __init__(self, id=None):
        client = pymongo.MongoClient("mongodb+srv://gian:gian123@cluster0.87opw.mongodb.net/test")
        db = client["gamecenterku"]
        self.col_payments = db["payments"]
        if id:
            self.id = ObjectId(id)
    
    def getId(self):
        return self.id
    
    def getUserId(self):
        get = self.col_payments.find_one({"_id":self.id}, {"user_id" : 1})
        if get == None:
            return None
        return get['user_id']
    
    def setUserId(self, user_id):
        new = { "$set": { "user_id": user_id } }
        return self.col_payments.update_one({"_id":self.id}, new)
        
    def getHarga(self):
        get = self.col_payments.find_one({"_id":self.id}, {"harga" : 1})
        if get == None:
            return None
        return get['harga']
    
    def setHarga(self, harga):
        new = { "$set": { "harga": harga } }
        return self.col_payments.update_one({"_id":self.id}, new)
    
    def getPayment_Method(self):
        get = self.col_payments.find_one({"_id":self.id}, {"payment_method" : 1})
        if get == None:
            return None
        return get['payment_method']
    
    def setPayment_Method(self, payment_method):
        new = { "$set": { "payment_method": payment_method } }
        return self.col_payments.update_one({"_id":self.id}, new)

    def getTelepon(self):
        get = self.col_payments.find_one({"_id":self.id}, {"telepon" : 1})
        if get == None:
            return None
        return get['telepon']
    
    def setTelepon(self, telepon):
        new = { "$set": { "telepon": telepon } }
        return self.col_payments.update_one({"_id":self.id}, new)
    
    def getEmail(self):
        get = self.col_payments.find_one({"_id":self.id}, {"email" : 1})
        if get == None:
            return None
        return get['email']

    def setEmail(self, email):
        new = { "$set": { "email": email } }
        return self.col_payments.update_one({"_id":self.id}, new)

    def getItem(self):
        get = self.col_payments.find_one({"_id":self.id}, {"item" : 1})
        if get == None:
            return None
        return get['item']
    
    def setItem(self, item):
        new = { "$set": { "item": item } }
        return self.col_payments.update_one({"_id":self.id}, new)

    def getStatus(self):
        get = self.col_payments.find_one({"_id":self.id}, {"status" : 1})
        if get == None:
            return None
        return get['status']
    
    def setStatus(self, status):
        new = { "$set": { "status": status } }
        return self.col_payments.update_one({"_id":self.id}, new)

    def getImg(self):
        get = self.col_payments.find_one({"_id":self.id}, {"img" : 1})
        if get == None:
            return None
        return get['img']
    
    def setImg(self, img):
        new = { "$set": { "img": img } }
        return self.col_payments.update_one({"_id":self.id}, new)

    def showAllPayments(self):
        arr = []
        for x in self.col_payments.find():
            arr.append(x)
        return arr
    
    def getData(self):
        return self.col_payments.find_one({"_id":self.id})
    
    def addPayments(self,games_id, user_id, harga, payment_method, email, telepon, item, status):
        dict_payments = {"games_id":games_id, "user_id":user_id, "harga":harga, "payment_method":payment_method, "email": email, "telepon":telepon, "item":item, "status":status}
        return self.col_payments.insert_one(dict_payments)
    
    def deletePayments(self):
        query = { "_id": self.id }
        return self.col_payments.delete_one(query)

if __name__ == "__main__":
    model = Payments()
    print(model.showAllPayments())

