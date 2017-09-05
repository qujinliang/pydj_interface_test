import sys
sys.path.append('../db_fixture')
import time
from mysql_db import DB


ISOTIMEFORMAT= '%Y-%m-%d %X'
#create data
datas = {
	
	'sign_event':[
		{'id':1,'name':'华为荣耀1发布会','`limit`':2000,'status':1,'address':'神州大厦','start_time':'2017-08-20 14:00:00','create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
		{'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'神州大厦','start_time':'2017-08-20 14:00:00','create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
		{'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'神州大厦','start_time':'2017-08-20 14:00:00','create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
		{'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'神州大厦','start_time':'2001-08-20 14:00:00','create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},\
		{'id':5,'name':'华为荣耀2发布会','`limit`':2000,'status':1,'address':'神州大厦','start_time':'2017-08-20 14:00:00','create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
	],
	'sign_guest':[
		{'id':1,'realname':'alen','phone':13711001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
		{'id':2,'realname':'has ign','phone':13711001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
		{'id':3,'realname':'tom','phone':13711001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':time.strftime(ISOTIMEFORMAT,time.localtime())},
	],
}

#Inster table datas
def init_data():
	db = DB()
	for table,data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table,d)
	db.close()

if __name__ == '__main__':
	init_data()