# 6-2. C언어

## 식별자 표기법

- **카멜 표기법(camel case)**: 첫 번째 단어 시작만 소문자로 표시하고 각 단어의 첫 글자는 대문자로 지정하는 표기법
  - 예: `inputFunction`
- **파스칼 표기법(pascal case)**: 각 단어의 첫 글자는 대문자로 지정하는 표기법
  - 예: `InputFunction`
- **스네이크 표기법(snake case)**: 여러 단어가 이어지면 단어 사이에 언더바를 넣는 표기법
  - 예: `input_function`
- **헝가리안 표기법(Hungarian case)**: 식별자 표기 시 두어에 자료형을 붙이는 표기법, int형일 경우 n, char형일 경우 c, 문자열일 경우 sz를 붙임
  - 예: `nScore`

## 연산자 우선순위

**암기법: 증산시 관비 논삼대** (증산 시장에서 관노비들이 논을 산대)

1. **증감 연산자**: `++`, `--`
   - 참고: `!`, `~` 은 예외로 우선순위가 높음
2. **산술 연산자**: `+`, `-`, `*`, `%`
3. **시프트 연산자**: `>>`, `<<`
4. **관계 연산자**: `<`, `<=`, `>`, `>=`, `!=`
5. **비트 연산자**: `&`, `|`, `^`
6. **논리 연산자**: `&&`, `||`
7. **삼항 연산자**: `(조건식) ? a : b`
8. **대입 연산자**: `=`, `+=`, `-=`, `*=`

## 1. 표준 함수

## (1) 문자열 함수

### ① `strcat`
문자열끼리 연결하는 함수 
- 사용법: `strcat(dest, src) => destsrc`

### ② `strcpy`
문자열을 복사하는 함수
- 사용법: `strcpy(dest, src) => dest`

### ③ `strcmp`
문자열을 비교하는 함수
- 사용법: `strcmp(s1, s2) => s1 > s2 : 1을 반환, s1 = s2 : 0을 반환, s1 < s2 : -1을 반환`

### ④ `strlen`
문자열의 길이를 알려주는 함수
- 사용법: `strlen(s) => s의 글자수`

### ⑤ `strrev`
문자열을 거꾸로 뒤집는 함수
- 사용법: `strrev(hello) => olleh`

### ⑥ `strchr`
문자열 내에 일치하는 문자가 있는지 검사하는 함수
- 사용법: `strchr(str, c) => str내에 c가 존재하는지 알려줌`

## (2) 유틸리티 함수

### ① `rand`
임의의 값을 생성하는 함수

### ② `srand(seed)`
seed값에 해당하는 난수 패턴 생성
- 예: `srand(time(NULL)) : 현재 시간으로 rand함수가 랜덤한 값을 가져오도록 함`

### ③ `time(NULL)`
현재 시간을 리턴

### ④ `atoi`
문자열을 정수형으로 변환 (ASCII to Integer)

### ⑤ `atof`
문자열을 실수형으로 변환 (ASCII to Floating Point)

### ⑥ `itoa`
정수형을 문자열로 변환 (Integer to ASCII)

## 2. 포인터

### (1) 포인터의 개념
포인터 : 변수의 주소값을 저장하는 공간  
개념 : `int a = 10; int *b = &a; => a == *b == *(&a)`

### (2) 배열과 포인터

```c
int a[3] = {1, 2};
int *p = a;
printf("%d %d %d", a[0], a[1], a[2]); // 1, 2, 0
printf("%d %d %d", *a, *(a+1), *(a+2)); // 1, 2, 0
printf("%d %d %d", *p, *(p+1), *(p+2)); // 1, 2, 0
printf("%d %d %d", p[0], p[1], p[2]); // 1, 2, 0
```

### (3) 2차원 배열과 포인터 배열

```c
int a[3][2] = {{1, 2}, {3, 4}, {5, 6}};
int *p[3] = {a[2], a[0], a[1]};

// 2차원 배열 a의 요소 접근
printf("2차원 배열 a의 요소:\n");
printf("%d %d\n", a[0][0], a[0][1]); // 1 2
printf("%d %d\n", a[1][0], a[1][1]); // 3 4
printf("%d %d\n", a[2][0], a[2][1]); // 5 6

// 포인터 배열 p를 통해 배열 a의 요소 접근
printf("\n포인터 배열 p를 통해 접근한 a의 요소:\n");
printf("%d %d\n", p[0][0], p[0][1]); // 5 6 (a[2])
printf("%d %d\n", p[1][0], p[1][1]); // 1 2 (a[0])
printf("%d %d\n", p[2][0], p[2][1]); // 3 4 (a[1])

// *a[0]을 통한 접근
printf("\n*a[0]을 통한 접근:\n");
printf("%d\n", *a[0]); // 1 (a[0][0])
printf("%d\n", *(a[0] + 1)); // 2 (a[0][1])

// *p[0]을 통한 접근
printf("\n*p[0]을 통한 접근:\n");
printf("%d\n", *p[0]); // 5 (a[2][0])
printf("%d\n", *(p[0] + 1)); // 6 (a[2][1])
```

### (4) 구조체와 포인터
### - 구조체는 일반 구조체 변수로 접근할 때는 .으로 접근하고, 구조체 포인터로 접근할 때는 ->로 접근한다.

```c
#include <stdio.h>

struct Student {
    char gender;
    int age;
};

int main() {
    struct Student s = {'F', 21};
    struct Student *p = &s;

    printf("%c %d\n", s.gender, s.age); // F 21
    printf("%c %d\n", (&s)->gender, (&s)->age); // F 21
    printf("%c %d\n", (*p).gender, (*p).age); // F 21
    printf("%c %d\n", p->gender, p->age); // F 21
    printf("%c %d\n", p[0].gender, p[0].age); // F 21

    return 0;
}
```
