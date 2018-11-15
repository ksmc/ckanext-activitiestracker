from ckan.plugins.toolkit import (request, BaseController, abort, render, c, h,
                                  _)
from ckan.logic import (ValidationError, NotAuthorized, NotFound, check_access,
                        get_action, clean_dict, tuplize_dict, parse_params)
import ckan.lib.navl.dictization_functions as dict_fns
import ckan.model as model
from ckan.controllers.api import ApiController

class ResourceTrackerController(BaseController):

    def _redirect_to_this_controller(self, *args, **kw):
        kw['controller'] = request.environ['pylons.routes_dict']['controller']
        return h.redirect_to(*args, **kw)
    
    def resource_tracker(self, dataset_id, resource_id):
        try:
            c.pkg_dict = get_action('package_show')(None, {'id': dataset_id})
            c.resource = get_action('resource_show')(None, {'id': resource_id})
            rec = get_action('resource_tracker_list')(None, {
                'resource_id': resource_id,
                'limit': 0
            })
        except NotAuthorized:
            abort(403)
        except NotFound:
            abort(404)
        return render(
            'resource-tracker/tracker.html',
            extra_vars={
                'logs': rec,
                'dataset_id': dataset_id,
                'resource_id': resource_id
            })
    
#     def get_resource_url(self, dataset_id, resource_id):
#         context = {'model': model, 'session': model.Session, 'user': c.user}
#         try:
#             c.pkg_dict = get_action('package_show')(None, {'id': dataset_id})
#             c.resource = get_action('resource_show')(None, {'id': resource_id})
#             
#             if request.method == 'GET':
#                 data = {
#                         'resource_id': resource_id,
#                         'package_id': c.pkg_dict['id'],
#                 }    
#                 get_action('resource_tracker_create')(context, data)
#                 h.redirect_to(c.resource['url'])
#             else:
#                 abort(400)
#         except NotAuthorized:
#             abort(403)
#         except NotFound:
#             abort(404)
#         except ValidationError, e:
#             h.flash_error(e.error_summary)