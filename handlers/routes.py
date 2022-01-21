

from flask import redirect
from controllers import defaultControler






def configure_routes(api, app):

    api.add_resource(defaultControler.HomeController, '/api/', endpoint="api")
    api.add_resource(defaultControler.TopNPlantsController, '/api/top/plants/', endpoint="api-top-plants")
    api.add_resource(defaultControler.AllStateAnnualGeneration, '/api/state-gen/all/')
    api.add_resource(defaultControler.FilterByStateCotroller, '/api/state-gen/filter/<state_abbreviation>/')


    @app.route('/')
    def default_api_home():
        return redirect("/api/")


    @app.errorhandler(404)
    def not_found(e):
        return redirect("/api/")


