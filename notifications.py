praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * number_of_characters
print(result)

advice = "Don't forget to ask for help"
advice = advice.upper()
number_of_characters = len(advice)
result = advice + "!" * number_of_characters
print(result)

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY")