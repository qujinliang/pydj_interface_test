import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class GetEventTest(unittest.TestCase):
	"""查询发布会"""
	def setUp(self):
		self.base_url = "http://127.0.0.1:8000/api/get_event_list/"

	def tearDown(self):
		print(self.result)

	def test_get_event_eid_error(self):
		'''id为空'''
		payload = {'id':921,'name':''}

		r = requests.get(self.base_url,params={'id':901})
		self.result= r.json()
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'query result is empty')

	def test_get_event_eid_success(self):
		'''查询成功'''
		payload = {'id':1,'name':''}

		r = requests.get(self.base_url,params={'id':1})
		self.result = r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')

	def test_get_event_name_error(self):
		'''name为空'''
		payload = {'id':'','name':'大煞风景'}

		r = requests.get(self.base_url,params={'name':'啦啦啦'})
		self.result = r.json()
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'query result is empty')

	def test_get_event_name_success(self):
		'''查询name成功'''

		r = requests.get(self.base_url,params={'name':'发布会'})
		self.result = r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')
		self.assertEqual(self.result['data'][0]['name'],u'华为荣耀1发布会')
		self.assertEqual(self.result['data'][0]['address'],u'神州大厦')

if __name__ == '__main__':
	test_data.init_data()
	unittest.main()





