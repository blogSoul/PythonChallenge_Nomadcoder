F

sequence type -> 열거형 타입이 존재합니다.

list : days = ["Mon, Tue, Wed, Thur, Fri"]

* 특성
common : 쉽게 사용 가능하다. (사용가능한 함수는 공식문서에서 확인하기)
Ex)
```
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print("Man" in days)
```
Mutable : 값을 바꿀 수 있다.
Ex)
```
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
days.append("Sat")
print(days)
days.reverse()
print(days)
```