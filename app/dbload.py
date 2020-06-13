from tinydb import TinyDB, Query

db = TinyDB('wordify.json')
cursor = Query()
count = db.search(cursor.counter > 0)[0].get("counter")
lst = []
while len(lst) == 0:
    count = count + 1
    lst = db.get(doc_id=count)
word = lst.get("word")
print(word)
db.remove(cursor.word == word)
db.update({'counter': count}, cursor.counter > 0)