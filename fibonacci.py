def fib(i=3):
	result = []
	result.append(0)
	result.append(1)

	for n in range(2,i):
		result.append(result[n-1] + result[n-2])

	print(result)


def main():
	count = input('請輸入要產生的費氏數列數量：')
	fib(int(count))

main()
