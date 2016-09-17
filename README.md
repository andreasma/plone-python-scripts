# getUser.py

This Python script connects via the api to Plone. It gets first a list of the current users of the Plone site with the 
full name, the ID, the email-address and the roles and writes the information to a csv-file.

Then he writes the username (ID) to a text file with new lines for every username.

The last step is a catalog search for the creators of tdf.templateuploadcenter.projects and write them
line by line to a text file.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' you could run this script with:

`./bin/instance -O testing run getUser.py`

