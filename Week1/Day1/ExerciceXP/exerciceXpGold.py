#Exercice 1
print("Execrice 1:")
print("Hello World\n" * 4 ,"I love Python\n" * 4)

#Exercice 2
print("Exercice 2:")
month = int(input("Enter the month: "))
if month not in range(1, 13):
    month = int(input("Invalid month, enter the month: "))

def switch_month(month):
    match month:
        case _ if month in range(3, 6):
            return "Spring"
        case _ if month in range(6, 9):
            return "Summer"
        case _ if month in range(9, 12):
            return "Autumn"
        case 12 | 1 | 2:
            return "Winter"

season = switch_month(month)
print(f"The season is: {season}")
