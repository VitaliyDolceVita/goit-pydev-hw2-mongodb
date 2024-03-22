
from pymongo.errors import ConnectionFailure, PyMongoError
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://goitlearn:4891@cluster0.o0ftgcm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
# Підключення до MongoDB
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



db = client["test"]
collection = db["cats"]

def read_all_cats():
    """ Виводить всі записи з колекції cats """
    try:
        for cat in collection.find():
            print(cat)
    except PyMongoError as e:
        print("Помилка читання з бази даних:", e)

def read_cat_by_name(name):
    """ Виводить інформацію про кота за ім'ям """
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кіт з ім'ям", name, "не знайдений.")
    except PyMongoError as e:
        print("Помилка при пошуку кота:", e)

def update_cat_age(name, age):
    """ Оновлює вік кота за ім'ям """
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.matched_count > 0:
            print("Вік кота оновлено.")
        else:
            print("Кіт з ім'ям", name, "не знайдений.")
    except PyMongoError as e:
        print("Помилка при оновленні віку кота:", e)

def add_feature_to_cat(name, feature):
    """ Додає нову характеристику до кота за ім'ям """
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.matched_count > 0:
            print("Характеристика додана.")
        else:
            print("Кіт з ім'ям", name, "не знайдений.")
    except PyMongoError as e:
        print("Помилка при додаванні характеристики:", e)

def delete_cat_by_name(name):
    """ Видаляє запис про кота за ім'ям """
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Кіт видалений.")
        else:
            print("Кіт з ім'ям", name, "не знайдений.")
    except PyMongoError as e:
        print("Помилка при видаленні кота:", e)

def delete_all_cats():
    """ Видаляє всі записи з колекції cats """
    try:
        collection.delete_many({})
        print("Всі коти видалені.")
    except PyMongoError as e:
        print("Помилка при видаленні всіх котів:", e)

# Приклади використання
read_all_cats()
# read_cat_by_name("barsik")
update_cat_age("barsik", 7)
read_all_cats()
add_feature_to_cat("barsik", "love playing")
# delete_cat_by_name("barsik")
# delete_all_cats()
