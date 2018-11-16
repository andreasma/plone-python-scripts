from plone import api

# Do this after installing all workflows
wf_tool = api.portal.get_tool(name='portal_workflow')
wf_tool.updateRoleMappings()
