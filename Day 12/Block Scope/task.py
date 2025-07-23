game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = "" # Declare and create that variable and initialize it
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Exercise
def is_prime(num):
    if num <= 1:  # 1 이하나 음수는 소수가 아닙니다.
        return False
    if num == 2:  # 2는 유일한 짝수 소수입니다. 특별히 처리합니다.
        return True
    if num % 2 == 0:  # 2보다 큰 짝수는 소수가 아닙니다.
        return False

    # 2를 제외한 홀수 약수만 확인하면 됩니다.
    # num의 제곱근까지만 확인해도 충분합니다. (약수는 항상 쌍으로 존재하므로)
    # 예를 들어 100의 약수가 10이라면 100/10=10. 만약 20이라면 100/20=5. 둘 중 하나는 제곱근 이하에 있습니다.
    # math.sqrt(num) 대신 num // 2 + 1 (또는 num의 절반까지만) 확인해도 괜찮습니다.
    # 여기서는 원래 코드에 가깝게 num-1까지로 설명하겠습니다.

    for i in range(3, int(num ** 0.5) + 1, 2):  # 3부터 num의 제곱근까지 홀수만 확인합니다. (효율성 향상)
        # 원래 코드처럼 2부터 num-1까지 해도 논리는 맞지만 비효율적입니다.
        # 여기서 중요한 건, 나누어 떨어지는 경우만 False를 반환하는 것입니다.
        if num % i == 0:  # 만약 'num'이 'i'로 나누어 떨어진다면
            return False  # 소수가 아닙니다. 즉시 False 반환.

    # 반복문이 끝났는데도 return False가 실행되지 않았다면
    # 이는 'num'이 어떤 약수로도 나누어 떨어지지 않았다는 의미입니다.
    # 따라서 'num'은 소수입니다.
    return True  # 모든 테스트를 통과하면 소수입니다.