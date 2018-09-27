import pickle
dbfile=open('people-pickle','rb')
db=pickle.load(dbfile)
print db
