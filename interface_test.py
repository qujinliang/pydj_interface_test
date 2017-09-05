import requests
import unittest

class GetEventListTest(unittest.TestCase):
	"""查询发布会接口测试"""
	
	def setUp(self):
		self.url = "http://127.0.0.1:8000/api/get_event_list/"

	def test_get_event_null(self):
		'''发布会id为空'''
		r = requests.get(self.url,params={'id':''})
		result = r.json()
		print(result)
		self.assertEqual(result['status'],10021)
		self.assertEqual(result['message'],'parameter error')

	def test_get_event_success(self):
		'''发布会id为1，查询成功'''
		r = requests.get(self.url,params={'id':'1'})
		result = r.json()
		print(result)
		self.assertEqual(result['status'],200)
		self.assertEqual(result['message'],'success')
		self.assertEqual(result['data']['name'],'华为荣耀10发布会')
		self.assertEqual(result['data']['address'],'神州数码大厦')
		self.assertEqual(result['data']['start_time'],'2017-08-02T14:07:11')

if __name__ == '__main__':
	unittest.main()

