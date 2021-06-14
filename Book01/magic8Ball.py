import random

def getAsnwer(asnwerNumber):
    if asnwerNumber == 1:
        return "It is certain."
    elif asnwerNumber == 2:
        return "It is  decidedly so"
    elif asnwerNumber == 3:
        return "Yes"
    elif asnwerNumber == 4:
        return "Reply  hazy try again"
    elif asnwerNumber == 5:
        return "Ask again later"
    elif asnwerNumber == 6:
        return "Concetrate and ask again"
    elif asnwerNumber == 7:
        return "My reply is no"
    elif asnwerNumber == 8:
        return "Outlook not so look"
    elif asnwerNumber == 9:
        return "Very doubbtful"

r = random.randint(1,9)
fortune =  getAsnwer(r)
print(fortune)