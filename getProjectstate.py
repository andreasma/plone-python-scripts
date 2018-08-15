from plone import api
import csv

portal = api.portal.get()

catalog = api.portal.get_tool(name='portal_catalog')

allextprojects = catalog(portal_type='tdf.extensionuploadcenter.eupproject')

for d in allextprojects:
     st = d.review_state
     url = ('/' .join (d.getObject().getPhysicalPath()))
     name = d.Title

     with open('extensionprojects.csv', 'ab') as et:
         pt = csv.writer(et, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         pt.writerow([name, st, url])
