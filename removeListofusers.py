from plone import api
import transaction

inputtextfile = raw_input("Please type in the name of the text file with the list of users, "
                          "you want to remove from the instance: ")

data = [line.strip() for line in open(inputtextfile, 'r')]

for item in data:
    print(item)
    api.user.delete(username=item)
    transaction.commit()
