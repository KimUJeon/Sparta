from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# movie = db.movies.find_one({'title':'매트릭스'})
# target_star = movie['star']
#
# same_movies = list(db.movies.find({'star':target_star}, {'_id': False}))
#
# for same in same_movies:
#     print(same['title'])

db.movies.update_one({'title':'매트릭스'}, {'$set':{'star':'0'}})
