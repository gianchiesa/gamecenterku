import pymongo

class Migrate:
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://gian:gian123@cluster0.87opw.mongodb.net/test")
        db = client["gamecenterku"]
        col_games = db["games"]
        dict_games = [
            {"games_id":"101", "game_name":"Mobile Legends", "user_id":"01293812", "image":"img/ml.jpeg", "dev":"moonton", "item":['7000,28 diamond,1', '15000,59 diamond,2', '20000,85 diamond,3', '75000,269 diamond,4', '141000,568 diamond,5', '474000,2010 diamond,6']},
            {"games_id":"102", "game_name":"Point Blank", "user_id":"01293812", "image":"img/pb.jpg", "dev":"ZEPETTO", "item":['10000,1200 Cash,1', '20000,2400 cash,2', '30000,3600 cash,3', '50000,6000 Cash,4', '100000,12000 Cash,5', '200000,24000 Cash,6']},
            {"games_id":"103", "game_name":"Honkai Impact 3rd", "user_id":"01293812", "image":"img/HI3.png", "dev":"Mihoyo", "item":['15000,65 Crystal,1', '75000,330 Crystal,2', '149000,710 Crystal,3', '299000,1430 Crystal,4', '739000,3860 Crystal,5', '1499000,8088 Crystal,6']},
            {"games_id":"104", "game_name":"PUBG", "user_id":"01293811", "image":"img/pubg.jpg", "dev":"Tencent", "item":['10000,50 UC,1', '30000,150 UC,2', '50000,250 UC,3', '100000,500 UC,4', '250000,1250 UC,5', '500000,2500 UC,6']},
            {"games_id":"105", "game_name":"Free Fire", "user_id":"01293811", "image":"img/ff.jpg", "dev":"Garena", "item":['10000,70 Diamonds,1', '20000,140 Diamonds,2', '50000,355 Diamonds,3', '100000,720 Diamonds,4', '200000,1450 Diamonds,5', '500000,3640 Diamonds,6']},
            {"games_id":"106", "game_name":"Valoran", "user_id":"21412411", "image":"img/v.png", "dev":"Riot Games", "item":['50000,420 Points,1', '80000,700 Points,2', '150000,1350 Points,3', '250000,2400 Points,4', '400000,4000 Points,5', '800000,8150 Points,6']},
        ]
        col_games.insert_many(dict_games)
        col_payments = db["payments"]
        dict_payments = [
            {"payments_id":"121", "games_id": "qwe", "user_id":"103", "harga":"3000", "payment_method":"OVO", "telepon": "08138247124", "item": "10 diamonds", "email" : "1000", "status" : "sukses", "img" : "uploads/qwe"}
        ]
        col_payments.insert_many(dict_payments)

        print(client.list_database_names())
        print(db.list_collection_names())

if __name__ == "__main__":
    m = Migrate()