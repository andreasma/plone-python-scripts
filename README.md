# getUser.py

This Python script connects via the api to Plone. It gets first a list of the current users of the Plone site with the 
full name, the ID, the email-address and the roles and writes the information to a csv-file.

Then he writes the username (ID) to a text file with new lines for every username.

The next step is a catalog search for the creators of tdf.templateuploadcenter.projects and write them
line by line to a text file.

In the following part the script creates a list of all active users of the site and in the last part a list of all 
inactive users.

In the end there are four new files inside the directory.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' 
you could run this script with:

`./bin/instance -O testing run getUser.py`


# addUser.py

This Python script connects via the api to Plone. It first asks the user to insert the
name of a csv file which contains a list of new users for the Plone website. Then the 
script asks for the name of the file where the updated list of current users after the
addition of new users should be written.

The csv file has to contain a new row per user with the comma seperated values in the
following order:

fullname, email-address, username

The script adds all current users including the newly added to a csv file in the end.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' 
you could run this script with:

`./bin/instance -O testing run addUser.py`


# getActiveuser.py

This Python script connects with Plone via its api. It looks first for the files from a former
run of the script, move them to a backup subdirectory and rename this backup directory with adding
the timestamp to the name.

It gets all users from the Plone site and write their full name, ID and email address to a new csv-file
in the next step. Then it write only the username/ID to a textfile row by row.

It looks for all users of the site that had already contributed to the main content of the site and 
write the ID/username of this person to a text file then.

The script generated out of the data of this files a list of active and non-active user of the site.
It substracts from the latter the group of administrators.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' 
you could run this script with:

`./bin/instance -O testing run getActiveuser.py`


# getPrereleases.py

This Python script searches in the Plone portal_catalog for extension and template releases that are only 
in the state of pre-releases. It write the title of all this pre-releases to a text file.

Usage: If your Plone instance get started with the command ./bin/instance start and is e.g. named 'testing' 
you could run this script with:

`./bin/instance -O testing run getPrereleases.py`
