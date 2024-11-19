questions = [
    [
        "who is adithya raghav","cricketer","coder","useless","painter","none",2
    ],
    [
        "who is  raghav","cricketer","coder","useless","painter","none",2
    ],
    [
        "who is adithya raghav","cricketer","coder","useless","painter","none",2
    ],
    [
        "who is adithya raghav","cricketer","coder","useless","painter","none",2
    ],
    [
        "who is adithya raghav","cricketer","coder","useless","painter","none",2
    ],
    [
        "who is adithya raghav","cricketer","coder","useless","painter","none",2
    ]
]
levels = [1000,2000,3000,4000,5000,10000,20000,40000,100000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"your question for RS. {levels[i]}")
    print(f" a. {questions[1]}   b.{questions[2]}")
    print(f"c.{questions[3]}    d.{questions[4]}")
    replay = int(input("enter your answer(1-4) or 0 to quit"))
    if replay == 0:
        quit
    if replay == question[-1]:
        print(f"congratulations you won RS. {levels[i]}")
    elif i == 1:
        money == 2000
    elif i == 4:
        money == 5000
    elif i == 8:
        money == 100000         
    else:
        print(f"better luck next time")
        break
print(f" your take home money is{levels[0]}")    
