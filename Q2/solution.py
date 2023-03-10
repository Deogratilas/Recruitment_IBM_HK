n = int(input())
allValid = True
errorCodes = []
for i in range(n):
    record = input().split()
    isValid = record[1] == "true"
    if not isValid:
        errorCodes.append(record[2])
    allValid = allValid and isValid

if allValid:
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))
