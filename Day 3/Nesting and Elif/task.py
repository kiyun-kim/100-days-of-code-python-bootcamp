print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")

BMI 계산기에 if/elif/else 문을 추가하여 계산된 BMI 값들을 해석하도록 만드세요.
만약 bmi가 18.5 미만이면 "underweight"이라고 출력하세요.
만약 bmi가 18.5 이상 25 미만이면 "normal weight"이라고 출력하세요.
만약 bmi가 25 이상이면 "overweight"이라고 출력하세요.

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")