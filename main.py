# Lesson14Homework
# THE BIO FUNCTION
def bio(name,born,pronoun):

    name = name.capitalize()
    print(name,"was born in",born)

    age = 2023 - born
    pronoun = pronoun.capitalize()
    print(pronoun,"will turn",age,"years old this year.")

    year = born + 67
    print(pronoun,"will be 67 in the year",year)

bio("stephen",1984,"he")
print("")
bio("mary",1990,"she")
print("")
bio("jane",2000,"she")

quit()