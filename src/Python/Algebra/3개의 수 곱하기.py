"""
프로그램 구상
input 받은 3개의 숫자를 곱한다.
"""


def main():
	try:
		def weather_retry():
			retry = input('다시 하시겠습니까?(y/n)> ')
			if retry == 'y':
				main()
			elif retry == 'n':
				exit()
			else:
				print('y, n 둘 중 하나로 입력해 주십시오.')
				weather_retry()

		input_1 = input('첫 번째 수 입력> ')
		input_2 = input('두 번째 수 입력> ')
		input_3 = input('세 번째 수 입력> ')

		input_1 = int(input_1)
		input_2 = int(input_2)
		input_3 = int(input_3)

		print(input_1 * input_2 * input_3)
		weather_retry()

	except ValueError:
		print('입력된 숫자가 적절한 형식이 아닌 것 같습니다. 다시 입력하십시오.')
		main()


print('숫자 곱하기에 오신 것을 환영합니다. 여기서는 총 3개의 숫자를 곱할 수 있습니다. ')
main()
