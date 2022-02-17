'''
ההבדל בין כל השלושה הוא:
ה list זוהי רשימה שיכולה להכיל גם int וגם str. ב list ניתן להציג כמה ערכים שנרצה. נאחסן רשימה בזיכרון ע"H שימוש בתווים --> []list

ב set מוצגים כל הערכים היחודיים כלומר אם ברשימה יש כמה int שחוזרים על עצמםת אז ה set ישאיר רק אחד מכל סוג. set יוגדר ע"י ()set

ה TUPLE מתנהג כמו רשימה אך לא ניתן לשנות בו ערכים. נגדיר tuple ע"י שימוש ב ()tuple

'''





userInput = int(input('Please enter an odd number: '))
start = -1
numOfSpaces = userInput
for i in range((userInput//2)+1):
    start +=2
    numOfSpaces -= 1
    space = '-' * numOfSpaces
    levels = space + ('*' * start)
    print(levels)

newStart = userInput
for i in range(userInput//2):
    newStart -= 2
    newSpace = '-' * (numOfSpaces+1)
    numOfSpaces += 1
    revLevels = newSpace + ('*' * newStart)
    print(revLevels)
