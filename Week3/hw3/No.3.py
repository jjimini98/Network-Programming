#3. 다음과 같이 구성되는 문자열을 구분 문자로 분리해 딕셔너리로 반환하는 함수를 포함하는 프로그램 작성
st = []
def splitor(string):
    string = string.split("&")
    for x in string:
        x= dict.fromkeys().split("=")

    return  x

print(splitor("led=on&motor=off&switch=off"))