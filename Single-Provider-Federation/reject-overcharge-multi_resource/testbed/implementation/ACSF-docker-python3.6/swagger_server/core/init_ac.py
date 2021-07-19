import csv
import logging

SERVICE_ID_FILE_NAME = "/usr/app/config/service_id_mapping.csv"
SERVICE_COST_FILE_NAME = "/usr/app/config/costs.csv"
MISC_FILE_NAME = "/usr/app/config/misc_config.csv"

class ServiceCost:
    def __init__(self, revenue, federation_cost):
        self.revenue = revenue
        self.federation_cost = federation_cost

class ACconfig:
    def __init__(self):
        self.services_num = 0
        self.service_id_mapping = {}
        self.service_costs = {}
        self.log_level = "DEBUG"
        self.error_on_unknown_state = False

    def load_service_id_mapping(self, service_id_mapping_file):
        self.services_num = 0
        with open(service_id_mapping_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass
                elif len(row) > 0:
                    service_id = row[0]
                    index = int(row[1])
                    self.service_id_mapping[service_id] = index
                    self.services_num += 1

                line_count += 1

    def load_service_costs(self, service_costs_file):
        with open(service_costs_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass
                elif len(row) > 0:
                    service_id = row[0]
                    revenue = float(row[1])
                    federation_cost = float(row[2])
                    self.service_costs[service_id] = ServiceCost(revenue, federation_cost)

                line_count += 1

    def load_misc_configs(self, misc_config_file):
        with open(misc_config_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='=')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass
                elif len(row) > 0:
                    row[0] = row[0].strip()
                    row[1] = row[1].strip()

                    if row[0] == "log_level":
                        valid_levels_names = {"CRITICAL": 50, "ERROR": 40, "WARNING": 30, "INFO": 20, "DEBUG": 10}
                        valid_levels_nums = {50, 40, 30, 20, 10}
                       
                        print("row[0] = ", row[0], "row[1] = ", row[1], flush=True)
                        if row[1] in valid_levels_names.keys():
                            self.log_level = valid_levels_names[row[1]]
                        elif int(row[1]) in valid_levels_nums:
                            self.log_level = int(row[1])
                        else:
                            self.log_level = "DEBUG"

                    elif row[0] == "error_on_unknown_state":
                        if row[1] == "True":
                            self.error_on_unknown_state = True


                line_count += 1


ac_config = None

def init():
    global ac_config

    ac_config = ACconfig()
    ac_config.load_misc_configs(MISC_FILE_NAME)
    ac_config.load_service_id_mapping(SERVICE_ID_FILE_NAME)
    ac_config.load_service_costs(SERVICE_COST_FILE_NAME)

    logging.basicConfig(filename='/var/log/ac.log', filemode='w', format='%(asctime)s %(levelname)s: %(message)s', level=ac_config.log_level)
    

