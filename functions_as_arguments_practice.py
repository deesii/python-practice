def calculate_tax_for_the_shire(grossPay):
    # The friendly Shire has a 20% tax rate
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    # Dodgy Mirkwood has a 90% tax rate
    return grossPay * 0.9


def calculate_tax_for_mordor(grossPay):
    # Terrible Mordor has a 90% tax rate plus a fixed tax of £500.
    return grossPay * 0.9 + 500


def report_pay(gross_pay, calculate_tax):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"


print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(4320.0, calculate_tax_for_mirkwood))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

#excercise II - Weather report


# Here are some instructions:

# Declare a function called report_weather that takes a temperature and a function as its two arguments
# Declare two other functions, each of which takes a temperature as an argument
# One is called as_sun_lover and it returns 'great' if the temp is 25 Celsius, or above. Otherwise it returns 'not great'
# One is called as_snow_lover and it returns 'great' if the temp is 0, or below. Otherwise it returns 'not great'
# Combine the functions to generate customised weather reports

def report_weather(temperature, weather_lover):
    thoughts = weather_lover(temperature)
    return f"The temperature was {temperature} and I thought it was {thoughts}"

def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "not great"

def as_snow_lover(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "not great"

#check
    
print("The sun lover:")
print(report_weather(45,as_sun_lover))

print("The snow lover:")
print(report_weather(45,as_snow_lover))

#further check

print(report_weather(24, as_sun_lover))

print(report_weather(25, as_sun_lover))

print(report_weather(1, as_snow_lover))

print(report_weather(0, as_snow_lover))