from plone import api


portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

results = catalog(portal_type=('tdf.templateuploadcenter.tuprelease',
                               'tdf.templateuploadcenter.tupreleaselink',
                               'tdf.extensionuploadcenter.euprelease',
                               'tdf.extensionuploadcenter.eupreleaselink'),
                  review_state= 'pre-release')

for d in results:
    with open('prereleases.txt', 'a+') as textfile:
        textfile.write(d.Title)
        textfile.write('\n')
