from plone import api


portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

results = catalog.unrestrictedSearchResults(portal_type=('tdf.templateuploadcenter.tupproject',
                                                         'tdf.extensionuploadcenter.eupproject'),
                                            review_state= 'private'
                                            )

for d in results:
    with open('privateprojects.txt', 'a+') as textfile:
        textfile.write(d.Title)
        textfile.write('\n')
