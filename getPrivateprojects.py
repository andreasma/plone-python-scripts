from plone import api
import csv


portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

privextproj = catalog.unrestrictedSearchResults(portal_type='tdf.extensionuploadcenter.eupproject',
                                                review_state ='private'
                                                )

privtempproj = catalog.unrestrictedSearchResults(portal_type='tdf.templateuploadcenter.tupproject',
                                                review_state= 'private'
                                                )

for d in privextproj:
    with open('privateextprojects.csv', 'ab') as csvfile:
        projecttitle = d.Title
        url = ('/' .join (d.getObject().getPhysicalPath()))
        privext = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        privext.writerow([projecttitle, url])


for d in privtempproj:
    with open('privatetempprojects.csv', 'ab') as csvfile:
        projecttitle = d.Title
        url = ('/' .join (d.getObject().getPhysicalPath()))
        privtemp = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        privtemp.writerow([projecttitle, url])
        
print ('done')
