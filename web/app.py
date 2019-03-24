import falcon

import mileages


api = application = falcon.API()

mileages = mileages.Resource()
api.add_route('/mileages', mileages)