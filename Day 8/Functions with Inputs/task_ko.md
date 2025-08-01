이전에 우리는 함수가 코드를 이름이 지정된 블록으로 묶어 나중에 반복적으로 사용할 수 있도록 해준다는 것을 보았습니다.

### PAUSE 1 - 검토
- `greet()`라는 이름의 함수를 생성하세요.
- 함수 내부에 3개의 `print` 문을 작성하세요.
- `greet()` 함수를 호출하고 코드를 실행하세요.

### 입력
새로운 함수를 만들 때 (정의할 때) 괄호 안에 변수 이름을 추가하면, 함수를 호출할 때 해당 입력값을 받을 수 있습니다. 

즉, 다른 입력값을 전달함으로써 함수의 동작을 호출할 때마다 다르게 변경할 수 있다는 뜻입니다.

```
# 함수 생성
def myFunction(input):
    print(f"안녕! {input}")
```
```
# 함수 사용
myFunction("Tommy") 
# 출력 결과는 "안녕! Tommy"가 됩니다
```

### 입력은 변수
입력을 받는 함수를 생성할 때는 전달된 데이터를 받을 변수 이름을 정의합니다.

입력 변수 이름, 예를 들어 이 코드에서 `def greet(name):`의 `name`은 매개변수(parameter)라고 부릅니다.

입력 변수의 값, 예를 들어 이전 `greet` 함수를 호출할 때의 `greet("Angela")`에서의 값 `Angela`는 인자(argument)라고 부릅니다.