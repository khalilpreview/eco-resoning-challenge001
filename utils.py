import json
import pandas as pd

"""

Comments Here ...

"""

class AnnualValues():

    def __init__(self):
    
        self.us_ws = pd.read_excel('data/egrid2016_data.xlsx', sheet_name='US16', header=0, usecols="A,F")

        self.plnt_ws = pd.read_excel('data/egrid2016_data.xlsx', sheet_name='PLNT16' , header=1, usecols="A,B,C,AL")
        self.plnt_ws_nan = self.plnt_ws.fillna(0)
        self.plnt_ws_nan['PLNGENAN'] = pd.to_numeric(self.plnt_ws_nan['PLNGENAN'], errors='coerce')
        self.plnt_ws_nan['PLNGENAN'] = self.plnt_ws_nan['PLNGENAN'].abs()
        self.plnt_ws_nan['PLNGENAN_Percent'] = ((self.plnt_ws_nan['PLNGENAN'] / self.plnt_ws_nan['PLNGENAN'].sum()) * 100)
        self.plnt_ws_sorted = self.plnt_ws_nan.sort_values(by='PLNGENAN', ascending=False)

        self.plnt_df_dict = self.plnt_ws_sorted.to_dict()
        
    def general_data(self):

        us_ws_dict = self.us_ws.to_dict()

        try:
            return {
                us_ws_dict['U.S. nameplate capacity (MW)'][0]: {
                    "detail":'U.S. nameplate capacity (MW)',
                    "value":us_ws_dict['U.S. nameplate capacity (MW)'][1]
                },
                us_ws_dict['U.S. annual net generation (MWh)'][0]: {
                    "detail":'U.S. annual net generation (MWh)',
                    "value":us_ws_dict['U.S. annual net generation (MWh)'][1]
                },
            }
        except AttributeError:
            return {
                "detail": "No data founded"
            }

    def top_n_plants(self):

        plnt_ws_sorted_head = self.plnt_ws_sorted.head(20)
        
        plnt_df_dict = plnt_ws_sorted_head.to_dict()

        default_dict_list = []

        pstatabb = plnt_df_dict['SEQPLT16']
        stngenan = plnt_df_dict['PSTATABB']
        pname = plnt_df_dict['PNAME']
        plngenan = plnt_df_dict['PLNGENAN']
        plngenan_per = plnt_df_dict['PLNGENAN_Percent']

        for key_1 in pstatabb:
            for key_2 in stngenan:
                for key_3 in pname:
                    for key_4 in plngenan:
                        for key_5 in plngenan_per:
                            if key_1 == key_2 == key_3 == key_4 == key_5:
                                default_dict_template = {
                                                            'SEQPLT16' : pstatabb[key_1],
                                                            'PSTATABB' : stngenan[key_2],
                                                            'PNAME' : pname[key_3],
                                                            'PLNGENAN' : plngenan[key_4],
                                                            'PLNGENAN_Percent' : plngenan_per[key_5]
                                                        }

            default_dict_list.append(default_dict_template)
                
        try:
            return default_dict_list

        except AttributeError:
            return {
                "detail": "No data founded"
            }

    def net_generation_by_federal_state(self):

        try:
            return self.plnt_df_dict

        except AttributeError:
            return {
                "detail": "No data founded"
            }

    def filtre_by_state(self, state):

        plnt_ws_result = self.plnt_ws_sorted[self.plnt_ws_sorted ['PSTATABB'].isin([(state).upper()])] 
        
        plnt_df_dict = plnt_ws_result.to_dict()
         
        try:
            return plnt_df_dict

        except AttributeError:
            return {
                "detail": "No data founded"
            }

