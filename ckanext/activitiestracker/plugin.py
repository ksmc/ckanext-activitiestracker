import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.authz as authz
from ckan.plugins.toolkit import get_action
from ckanext.activitiestracker.logic import action
from ckanext.activitiestracker.logic import auth

class ActivitiesTrackerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'activitiestracker')
        
    # IActions

    def get_actions(self):
        return {
            'resource_tracker_list': action.resource_tracker_list,
            'resource_tracker_create': action.resource_tracker_create,
        }
    
    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'resource_tracker_list': auth.resource_tracker_list,
            'resource_tracker_create': auth.resource_tracker_create,
        }
        
    # IRoutes

    def before_map(self, m):
        m.connect(
            'resource_tracker',
            '/dataset/{dataset_id}/resource/{resource_id}/log',
            controller=
            'ckanext.activitiestracker.controller:ResourceTrackerController',
            action='resource_tracker',
            ckan_icon='users')
#         m.connect(
#             'get_resource_url',
#             '/dataset/{dataset_id}/resource/{resource_id}/url',
#             controller=
#             'ckanext.activitiestracker.controller:ResourceTrackerController',
#             action='get_resource_url')
        return m
    