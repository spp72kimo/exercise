
def find_max(a_list=[]):
	if not a_list:
		return 0	
	max_value = a_list[0]
	for i in range(len(a_list)):
		if a_list[i] > max_value:
			max_value = a_list[i]
	return max_value
				

# num = input('請輸入數字：')
# num = num.split()
# for i in range(len(num)):
# 	num[i] = int(num[i])

# print(num)
print('最大值是：', find_max([]))