grader = int(input("Hvor mange grader er det ute? "))

if grader < 15:
    print("ta på jakke")
    type = input("Regner det?")
    if type.lower() == "ja":
        print("ta med paraply")
else:
    print("ha en fin dag i varmen!")



i = 0
while i < 20:
    i += 2
    print(i)