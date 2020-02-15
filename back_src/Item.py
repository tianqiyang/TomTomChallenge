

class item:

	def __init__(self, business, item_name, description, expire_time, price, quantity, is_raw):
		"""
			args:
				business: the business object
				item_name: the name of the item
				expire_time: expiry time
				price: the price for this item
				is_raw: false if the item is cooked
		"""
		self.business_uid = business.local_uid
		self.item_name = item_name
		self.expire_time = expire_time
		self.description = description
		self.price = price
		self.quantity = quantity
		self.is_raw = is_raw
		self.allergy_info = list()

	def setUID(uid)：
		self.item_uid = uid

	def addAllergyInfo(info):
		self.allergy_info.append(info)

