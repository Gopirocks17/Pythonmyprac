import pickle
dbfile=open('people-pickle','rb')
db=pickle.load(dbfile)
dbfile.close()

db['tom']['name'] = 'Tom Tom'

dbfile=open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()
