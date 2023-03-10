n = int(input())
sizes = input().split()
m = int(input())
requests = input().split()

# Create a dictionary to count the number of T-shirts available for each size
count = {}
for size in sizes:
    if size in count:
        count[size] += 1
    else:
        count[size] = 1

# Check if all requests can be fulfilled
for req in requests:
    found = False
    for size in sorted(count.keys()):
        if size >= req:
            found = True
            count[size] -= 1
            if count[size] == 0:
                del count[size]
            break
    if not found:
        print("No")
        break

if found:
    print("Yes")
