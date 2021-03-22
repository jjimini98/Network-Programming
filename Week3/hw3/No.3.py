#3. 다음과 같이 구성되는 문자열을 구분 문자로 분리해 딕셔너리로 반환하는 함수를 포함하는 프로그램 작성
def splitor(string):
    di = {}
    st = []

    string = string.split("&")

    for x in string:
      st.append(x.split("="))

    for t in st:
        di[t[0]] = t[1]

    return  di

print(splitor("led=on&motor=off&switch=off"))