from utils import AnnualValues
from flask_restful import Resource


annual_value = AnnualValues()


class HomeController(Resource):

    def get(self):
        return {
            "detail" : "This API give information about Annual net generation of power plants of the U.S (2016)",
            "genral_data": annual_value.general_data(),
            "api_valid_end_points":{
                "/api/" : "API home",
                "/api/top/plants/" : "Top N plants",
                "/api/state-gen/all/" : "Show absolute value and percentage of the annual net generation for all federal state",
                "/api/state-gen/filter/<state_abbreviation>/": "Filter state abbreviation"
                }   
            } 

class TopNPlantsController(Resource):

    def get(self):
        return {
            "detail" : "The top N plants in terms of annual net generation",
            "general_data": annual_value.top_n_plants()
        }


class AllStateAnnualGeneration(Resource):

    def get(self):

        return {
            "detail" : "Show absolute value and percentage of the annual net generation for all federal state",
            "general_data": annual_value.net_generation_by_federal_state()
        }


class FilterByStateCotroller(Resource):

    def get(self, state_abbreviation):

        return {
            "detail" : "Filter by federal state abbreviation",
            "general_data": annual_value.filtre_by_state(state_abbreviation)
        }

