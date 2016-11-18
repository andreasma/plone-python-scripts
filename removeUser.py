from plone import api
import transaction


listremoveusers = raw_input("Please type in the name of the text file with the usernames (only this names and"
                            "only one name per line), which you want to delete and remove from the Plone"
                            "instance: ")

portal = api.portal.get()

with open(listremoveusers, 'r') as f:
    for line in f:
        user=line
        api.user.delete(username=user)
        transaction.commit()
    
