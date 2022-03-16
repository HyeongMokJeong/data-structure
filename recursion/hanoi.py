# 하노이의 탑

def move(no: int, x: int, y: int) -> None: 
    # no는 옮겨야 할 원반의 개수, x는 시작 기둥의 번호, y는 목표 기둥의 번호
    if no > 1:
        move(no - 1, x, 6 - x - y)
        # 마지막 원반 빼고 1번 기둥에서 2번(가운데) 기둥으로

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)
        # 마지막 원반 빼고 2번(가운데) 기둥에서 3번 기둥으로

print('하노이의 탑을 구현합니다.')
n = int(input('원반의 개수를 입력하세요.: '))

move(n, 1, 3)