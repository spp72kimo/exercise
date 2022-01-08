def fib(n=0):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


def show_fib(i=2):
	result = []
	result.append(0)
	result.append(1)

	for n in range(2,i):
		result.append(result[n-1] + result[n-2])

	print(result)

def main():
	max_value = input('請輸入要產生的費氏數列數量：')
	show_fib(int(max_value))
	while True:
		count = input('請輸入需要第幾個的數字：')
		try:
			count = int(count)
			if count < 0:
				print('需要大於0')
				continue
			else:
				break
		except:
			print('請輸入數字！')
	ans = fib(count-1)
	print('第', count, '項：', ans)

main()
