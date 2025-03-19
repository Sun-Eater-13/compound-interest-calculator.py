control=0
while   control==0:
    try:
        initial=float(input("Input inital investment (no more than 2 digits after the decimal): "))
        if initial>=0:
            initial1 = round(initial, 2)
            if initial1==initial:
                control+=1
            else:
                print("Input proper number")
        else:
            print("Input proper number")
    except ValueError:
        print("Input proper number")
final=initial
while   control==1:
    try:
        deposit=float(input("Input additional deposit (no more than 2 digits after the decimal): "))
        if deposit>=0:
            deposit1 = round(deposit, 2)
            if deposit1==deposit:
                control+=1
            else:
                print("Input proper number")
        else:
            print("Input proper number")
    except ValueError:
        print("Input proper number")
while   control==2:
    try:
        period=str(input("Is the addtional deposit annual and monthly (A/M)? "))
        if period=="A" or period=="M":
            control+=1
        else:
            print("Input A or M")
    except ValueError:
        print("Input proper letter")
while   control==3:
    try:
        time=int(input("Input number of periods (no digits after the decimal): "))
        if time>0:
            control += 1
        else:
            print("Input proper number of years")
    except ValueError:
        print("Input proper number of years")
while   control==4:
    try:
        interest=float(input("Input interest rate (in %, no more than 2 digits after the decimal): "))
        if interest>=0:
            interest1 = round(interest, 2)
            if interest1==interest:
                control+=1
                interest=interest/100
            else:
                print("Input proper number")
        else:
            print("Input proper number")
    except ValueError:
        print("Input proper number")
for i in range (1, time + 1):
    final=round(final * (1 + interest) + deposit, 2)
if period=="A":
    print(f"With initial investment {initial}, additional annual deposit {deposit} and {interest* 100}% interest rate after {time} years you will have {final}")
else:
    print(f"With initial investment {initial}, additional monthly deposit {deposit} and {interest * 100}% interest rate after {time} months you will have {final}")
