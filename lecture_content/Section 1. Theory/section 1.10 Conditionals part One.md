## section 1.10 Conditionals part One

if - else 문으로 조건을 만들 수 있습니다.
Ex) 
```
def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b  
    else:
        return None
```
python에선 is, is not이 존재합니다.
is문는 object identity를 의미합니다.
is not문은 negated object identity를 의미합니다.