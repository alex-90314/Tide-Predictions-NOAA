with open('Tide_Info.csv') as f:
    data = f.readlines()

    for line in data:

        line = line.strip()
        vars = line.split(" ")

        date, time, predict = vars

        print(f"On {date} @ {time} the tide will be {predict}")