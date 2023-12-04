import re


def day2():
    with open("2023/day2.txt") as file:
        index = 1
        gameresult = []

        for game in file:
            red = green = blue = power = 0
            split = game.split(": ")
            replace = split[1].replace(";", ",")
            gamelist = [replace.split(", ")]
            for item in gamelist:
                for individual in item:
                    if individual.find("red") != -1:
                        if int(re.sub(r"\D", "", individual)) > red:
                            red = int(re.sub(r"\D", "", individual))
                    if individual.find("green") != -1:
                        if int(re.sub(r"\D", "", individual)) > green:
                            green = int(re.sub(r"\D", "", individual))
                    if individual.find("blue") != -1:
                        if int(re.sub(r"\D", "", individual)) > blue:
                            blue = int(re.sub(r"\D", "", individual))
            power = red * green * blue
            gameresult.append((index, red, green, blue, power))
            index += 1

        gameid = power = 0
        for item in gameresult:
            if item[1] <= 12 and item[2] <= 13 and item[3] <= 14:
                gameid += item[0]
        for item in gameresult:
            power += item[4]
        print(gameid)
        print(power)


day2()  # 2449, 63981
