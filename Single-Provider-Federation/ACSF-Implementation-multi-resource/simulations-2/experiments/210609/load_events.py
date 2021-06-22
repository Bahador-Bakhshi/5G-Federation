import csv
import parser
import Environment

def get_service(service_id):
    for service in Environment.domain.services:
        if service_id == service.nsid:
            return service

    return None


def get_event_reqs():
    event_file_name = "./events.txt"

    all_req = []

    with open(event_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            elif len(row) > 0:
                ts = float(row[0])
                service_type = row[1]
                ht = float(row[2])
            
                service_id = -1
                if service_type == "NS1":
                    service_id = 0
                elif service_type == "NS2":
                    service_id = 1

                service = get_service(service_id)
                req = Environment.Request(ts, ts + ht, service.revenue, service_id)
                req.add_required_capacity(Environment.traffic_loads[service_id].service)
                all_req.append(req)

            line_count += 1

    #for req in all_req:
    #    print(req)

    return all_req

