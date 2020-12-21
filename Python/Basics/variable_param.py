def print_n_times(n, *values):  # 가변 매개변수 함수
    # do it for n time(s)
    for i in range(n):

        for value in values:
            print(value)
        print()  # just a line switch


print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
