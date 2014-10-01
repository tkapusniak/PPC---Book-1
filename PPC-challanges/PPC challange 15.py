#PPC challange 15
count = 0
attempt = input('Password? ')
while attempt != "changeme":
    if attempt != "changeme":
        count += 1
        print("Nope. Try again.", str(count))
    attempt = input('Password? ')
print("Accepted")
