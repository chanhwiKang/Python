######## 최빈값 구하기 ########
############################

# 아래는 내가 푼것


# A.count(obj)		
# 배열에서 obj로 지정한 내용과 동일한 항목을 찾아 그 개수를 리턴 합니다.

# A.remove(obj)		
# 배열에서 obj로 지정한 내용과 동일한 첫 항목을 찾아 삭제하고 나머지를 좌측으로 이동시킵니다.  None type.

# A.remove(obj)		
# 배열에서 obj로 지정한 내용과 동일한 첫 항목을 찾아 삭제하고 나머지를 좌측으로 이동시킵니다.  None type.

def solution(array):
    i = 0
    a = 0
    list_i = []
    list_icnt = []
    array.sort()

    while len(array) > 0: # array의 항목이 0이면 반복 멈춤
        if array.count(i) > 0 : # i가 list안에 있으면
            list_i.append(i) #list_i = 원소
            list_icnt.append(array.count(i)) # list_icnt = 원소의 개수를 저장
            array.remove(i) # list에서 i의 값과 같은 첫 항목을 찾아 삭제
            while array.count(i) > 0:
                array.remove(i)
        i += 1
   
    if list_icnt.count(max(list_icnt)) != 1: # 최빈값이 여러개면 return -1
        return -1
    else: # 최빈값이 하나라면
        for i in list_icnt:
            if max(list_icnt) == i:
                return list_i[a]
            else: 
                a +=1
                
# 다른 사람의 코드(dictionay, set을 사용한 코드)

def solution(array):
    keys = set(array)
    dict = {}
    max_freq = []
    for key in keys:
        dict[key] = array.count(key)
    for key in keys:
        if dict[key] == max(dict.values()):
            max_freq.append(key)
    if len(max_freq) > 1:
        answer = -1
    else:
        answer = max_freq[0]
    return answer
        
