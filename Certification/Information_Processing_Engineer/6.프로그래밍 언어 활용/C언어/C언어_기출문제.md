# C언어 기출문제 (p6-77 ~ p6-109)

## 05 다음은 C언어 코드이다. 출력 결과를 쓰시오.

```c
#include <stdio.h>
int main() {
    char *p = "KOREA";
    printf("%s\n", p); 
    printf("%s\n", p+3);
    printf("%c\n", *p);
    printf("%c\n", *(p+3));
    printf("%c\n", *p+2);
    return 0;
}
```
### - 정답 : KOREA, EA, K, E, M

## 12 빈칸에 연산자를 써서 정수를 역순으로 출력하는 프로그램을 완성하시오.
```c
#include <stdio.h>
int main() {
    int number = 1234;
    int div = 10;
    int result = 0;
    while (number != 0) {
        result = result * div;
        result = result + number % div;
        number = number / div;
    }
    printf("%d", result);
    return 0;
}
```

## 13 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.
```c
#include <stdio.h>
int isPrime(int number) {
    int i;
    for (i=2; i<number; i++) {
        if (number % i == 0) return 0;
    }
    return 1;
}

int main() {
    int number = 13195, max_div = 0, i;
    for (i=2; i<number; i++) {
        if (isPrime(i) == 1 && number % i == 0) {
            max_div = i;
        }
    }
    printf("%d", max_div);
    return 0;
}
```
### - 정답 : 29

## 17 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.
```c
#include <stdio.h>
int calc(int w, int h, int j, int i) {
    if(i>=0 && i<h && j>=0 && j<w)
        return 1;
    return 0;
}

int main() {
    int field[4][4] = {{0,1,0,1}, {0,0,0,1}, {1,1,1,0}, {0,1,1,1}};
    int mines[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};

    int w = 4, h = 4;
    int i, j, k, l;

    for(l=0; l<h; l++) {
        for(k=0; k<w; k++) {
            if(field[l][k] == 0)
                continue;
            for(i=l-1; i<=l+1; i++) {
                for(j=k-1; j<=k+1; j++) {
                    if(calc(w, h, j, i) == 1)
                        mines[i][j] += 1;
                }
            }
        }
    }

    for(l=0; l<h; l++) {
        for(k=0; k<w; k++) {
            printf("%d ", mines[l][k]);
        }
        printf("\n");
    }

    return 0;
}
```
### - 정답 : 1 2 2 1 , 2 4 4 3 , 2 4 3 3 , 1 3 3 2 

## 18 다음은 C언어 소스 코드이다. 출력 결과를 쓰시오.
```c
#include <stdio.h>
int main() {
    int i, j, k, s;
    int el = 0;
    for (i=6; i<=30; i++) {
        s = 0;
        k = i / 2;
        for (j=1; j<=k; j++) {
            if (i % j == 0) {
                s = s + j;
            }
        }
        if (s == i) {
            el++;
        }
    }
    printf("%d", el);
    return 0;
}
```
### - 정답 : 2








