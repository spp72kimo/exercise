# 計算清單內相同商品的數量，
# 並且以字典回傳

def count_products(data):
	result = {}
	price = []
	products = [d.split() for d in data]
	name = [p[0] for p in products]
	for n in name:
		price = [int(p[1]) for p in products if p[0] == n]
		total = sum(price)
		result[n] = total

	return result







data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
count_products(data)