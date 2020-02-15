import json
from pathlib import Path

def find_all_business_with_raw(business_list):
	"""
		This function returns all business with raw items

		Args:
			business_list: the list of all businesses
		Return:
			the list of business with raw items
	"""
	res_list = list()
	for business in business_list:
		item_list = business.posts
		for item in item_list:
			if item.is_raw:
				res_list.append(business)
				break;
	return res_list

def find_all_business_with_cooked(business_list):
	"""
		This function returns all business with cooked items

		Args:
			business_list: the list of all businesses
		Return:
			the list of business with cooked items
	"""
	res_list = list()
	for business in business_list:
		item_list = business.posts
		for item in item_list:
			if not item.is_raw:
				res_list.append(business)
				break;
	return res_list

def find_all_raw_item_in_business(business):
	"""
		This function returns the list of all raw items in a business
		
		Args:
			business: the business object to be checked
		Return:
			the list of all raw items from the business
	"""
	res_list = list()
	for item in business.posts:
		if item.is_raw:
			res_list.append(item)
	return res_list

def find_all_cooked_item_in_business(business):
	"""
		This function returns the list of all coocked items in a business
		
		Args:
			business: the business object to be checked
		Return:
			the list of all raw items from the business
	"""
	res_list = list()
	for item in business.posts:
		if not item.is_raw:
			res_list.append(item)
	return res_list

def read_file_in_data(file_name, read_or_write):
	"""
		This function returns the loaded file in data folder

		Args:
			file_name: the name of the file to be opened
			read_or_write: 0 if read only, 1 if write only, 2 if addition
	"""
	path = Path('..') / 'data' / file_name
	if read_or_write == 0:
		with open(path, 'r') as f:
			return f
	elif read_or_write == 1:
		with open(path, 'w') as f:
			return f
	else:
		with open(path, ''a) as f:
			return f
	return None

def 
