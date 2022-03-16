# 유클리드 호제법

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return gcd(y, x%y)

if __name__ =='__main__':
    print('최대 공약수를 구합니다.')
    x = int(input('첫 번째 정수값을 입력하세요.: '))
    y = int(input('두 번째 정수값을 입력하세요.: '))
    print(f'두 수의 최대 공약수는 {gcd(x, y)}입니다.')