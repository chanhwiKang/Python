# 빈 자리는 _로 두고, 오른쪽 정렬을 하되 10자리 확보
print(f"{500:_>10}") # _ = 빈공간, > = 오른쪽 정렬, 10 = 10자리 확보

# 양수일땐 +, 음수일땐 - 붙이기
print(f"{500: >+10}")
print(f"{-500: >+10}")

# 3자리마다 , 찍어주기
print(f"{1000000000:,}")

# 3자리마다 ','찍어주기, + - 붙이기
print(f"{1000000000:+,}")

# 3자리마다 ','찍어주기, + - 붙이기, 자리확보, 오른쪽 정렬
print(f"{10000000000:^<+30,}")

# 소수점 출력
print(f"{5/3:f}")
print(f"{5/3:.2f}")