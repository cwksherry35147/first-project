List = []
Running = True

while(Running ==True):
    user = input("Please enter a number!")

    if(user == "stop"):
        break

    user = int(user)
    List.append(user)
    print(List)

Steps_Total = len(List)
i = 0
Total = 0

while(i != Steps_Total):
    Total += List[i]
    i += 1

Total_avg = Total / Steps_Total
print(Total_avg)


