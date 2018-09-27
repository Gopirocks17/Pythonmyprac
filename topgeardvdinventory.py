import mysql.connector


class dvdrecord:
	def __init__(self):
		try: 
			global mydb
			global mycursor
			mydb= mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='DVD_Record')
			mycursor=mydb.cursor()
			if(mydb):
				print('db connected')
		except:
			mydb= mysql.connector.connect(user='root',password='root',host='127.0.0.1')
			mycursor= mydb.cursor()
			mycursor.execute("CREATE DATABASE IF NOT EXISTS DVD_Record")
			mydb= mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='DVD_Record')
			if(mydb):
				print('db connected')
			
		
	def createtb(self):
		mycursor.execute("CREATE TABLE IF NOT EXISTS DVD_Records(Title VARCHAR(255) PRIMARY kEY,Star_name VARCHAR (255),Year_of_release VARCHAR(255),Genre VARCHAR(255))")
		
	def add_dvd(self,til,sn,year,genr):
		sql="INSERT INTO DVD_Records(Title,Star_name,Year_of_release,Genre) VALUES (%s,%s,%s,%s)"
		val=(til,sn,year,genr)
		mycursor.execute(sql,val)
		mydb.commit()
		print("\nRecord added")

	def search_dvd(self,sear):
		sql="SELECT * FROM DVD_Records WHERE TITLE=%s"
		mycursor.execute(sql,(sear,))
		result=mycursor.fetchall()
		if result==[]:
			print("Not Found in the database")
			return 1
		else:
			print("\nDetails\nTitle Name:{0}\nStar name:{1}\nYear of release:{2}\nGenre:{3}".format(result[0][0],result[0][1],result[0][2],result[0][3]))
			return 0
	def modify_dvd(self,modv,titl,upd):
		if(upd=='Title'):
			sql="UPDATE DVD_Records SET Title=%s WHERE Title=%s"
			mycursor.execute(sql,(modv,titl))
		elif(upd=='Star_name'):
			sql="UPDATE DVD_Records SET Star_name=%s WHERE Title=%s"
			mycursor.execute(sql,(modv,titl))
		elif(upd=='Year_of_release'):
			sql="UPDATE DVD_Records SET Year_of_release=%s WHERE Title=%s"
			mycursor.execute(sql,(modv,titl))
		elif(upd=='Genre'):
			sql="UPDATE DVD_Records SET Genre=%s WHERE Title=%s"
			mycursor.execute(sql,(modv,titl))
		mydb.commit()
		print("\nupdated")
	def del_dvd(self,titl):
		sql="DELETE FROM DVD_Records WHERE Title=%s"
		mycursor.execute(sql,(titl,))
		mydb.commit()
		print("\nDeleted")	
	def close_dvd(self):
		mycursor.close()
		mydb.close()	
		

if __name__=='__main__':
	d1=dvdrecord()
	d1.createtb()
	a=input("1.Add a DVD\n2.Search by Title\n3.Modify a DVD\n4.Delete a DVD\n5.Exit\n(Enter Number):")
	while(a!=5):
		if(a==1):
			title=raw_input('Enter title of DVD\n')
			sname=raw_input('Enter star name of DVD\n')
			yearof=raw_input('Enter year of DVD\n')
			genre=raw_input('Enter Genre of DVD\n')
			d1.add_dvd(title,sname,yearof,genre)
		elif(a==2):
			se=raw_input("Enter Title of DVD:")
			d1.search_dvd(se)
		elif(a==3):
			titl=raw_input("which record you wants to modify(Enter Title):")
			if(d1.search_dvd(titl)):
				pass	
			else:
				d={1:'Title',2:'Star_name',3:'Year_of_release',4:'Genre'}
				print(d)
				attr1=int(raw_input("Which attribute to modify(Enter number):"))
				while(attr1 not in [1,2,3,4]):
					print("Enter valid value")
					attr1=int(raw_input("Which attribute to modify(Enter number):"))
				mod1=raw_input("Enter modify value:")
				d1.modify_dvd(mod1,titl,d[attr1])
		elif(a==4):
			drec=raw_input("Which record you want to delete(Enter Title):")
			if(d1.search_dvd(drec)):
				pass
			else:
				d1.del_dvd(drec)
		else:
			print("\nEnter Valid Input")
		a=input("\n1.Add a DVD\n2.Search by Title\n3.Modify a DVD\n4.Delete a DVD\n5.Exit\n(Enter Number):")
	d1.close_dvd()	
	
	

