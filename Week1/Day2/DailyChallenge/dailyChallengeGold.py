from datetime import datetime

def birthday_cake(candles):
    # ensure at least one candle
    c = "i" * (candles or 1)
    return (
        "   ___" + c + "___\n"
        "  |:H:a:p:p:y:|\n"
        "__|___________|__\n"
        "|^^^^^^^^^^^^^^^^^|\n"
        "|:B:i:r:t:h:d:a:y:|\n"
        "|                 |\n"
        "~~~~~~~~~~~~~~~~~~~\n"
    )

birthdate = input("Enter your birthdate Date (DD/MM/YYYY): ").strip() # i did not use parse date to make it sample 
#or 
# birthdate_parse= datetime.strptime(birthdate, "%d/%m/%Y").date()

birth_year = int(birthdate.split('/')[-1])

current_year = datetime.now().year #current year

# calculate age
age = current_year - birth_year

# to get last digit of age
last_digit = int (str(age)[-1]) # or using ag % 10

#leap year
is_leap_year = (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0)

# Display cake(s)
if is_leap_year:
    print("Leap year!")
    print((birthday_cake(last_digit) + "\n")* 2) # print two cakes, with a blank line between them

else:
    birthday_cake(last_digit)
