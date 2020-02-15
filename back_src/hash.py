
import hashlib

def sha256_hash(str):
	"""
		Args:
			the string to be hashed
	
		Return:
			the hashed hexcode

		Raises:
			TypeError
	"""
	return hashlib.sha256(bytes(str, encoding='utf-8')).hexdigest()