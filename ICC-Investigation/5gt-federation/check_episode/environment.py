import sys
import numpy as np
import random
import math

class Env:
    def __init__(self, cpu, memory, disk,
            f_cpu=math.inf, f_memory=math.inf, f_disk=math.inf):
        self.cpu = cpu
        self.disk = disk
        self.memory = memory
        self.f_cpu = f_cpu
        self.f_disk = f_disk
        self.f_memory = f_memory
        self.time = float(0)
        self.capacity = [int(cpu), int(memory), int(disk)]
        self.f_capacity = [int(f_cpu), int(f_memory), int(f_disk)] if\
            f_cpu != math.inf else [math.inf, math.inf, math.inf]
        self.profit = float(0)
        self.service_cpu = []
        self.service_disk = []
        self.service_memory = []
        self.service_arrival_time = []
        self.service_length = []
        self.federated_service_cpu = []
        self.federated_service_disk = []
        self.federated_service_memory = []
        self.federated_service_arrival = []
        self.federated_service_length = []
        self.total_num_services = int(0)


    def reset(self):
        self.cpu = float(self.capacity[0])
        self.memory = float(self.capacity[1])
        self.disk = float(self.capacity[2])
        self.f_cpu = float(self.f_capacity[0])
        self.f_memory = float(self.f_capacity[1])
        self.f_disk = float(self.f_capacity[2])
        self.time = float(0)
        self.profit = float(0)
        self.service_cpu = []
        self.service_disk = []
        self.service_memory = []
        self.service_arrival_time = []
        self.service_length = []
        self.federated_service_cpu = []
        self.federated_service_disk = []
        self.federated_service_memory = []
        self.federated_service_arrival = []
        self.federated_service_length = []
        self.total_num_services = int(0)

    def current_capacity(self):
        return [int(self.cpu), int(self.memory), int(self.disk)]

    def current_federation_capacity(self):
        return [int(self.f_cpu), int(self.f_memory), int(self.f_disk)]

    def calculate_state(self):
        f_state = 0 if self.f_cpu == math.inf else \
            int((self.f_cpu*self.f_capacity[1]*self.f_capacity[2]) +\
                    (self.f_memory*self.f_capacity[2]) + (self.f_disk-1))
        return int((self.cpu*self.capacity[1]*self.capacity[2]) + (self.memory*self.capacity[2]) + (self.disk-1) + f_state)

    def capacity_to_state(self,cpu,memory,disk,):
        f_state = 0 if self.f_cpu == math.inf else \
            int((self.f_cpu*self.f_capacity[1]*self.f_capacity[2]) +\
                    (self.f_memory*self.f_capacity[2]) + (self.f_disk-1))
        return int((cpu*self.capacity[1]*self.capacity[2]) + (memory*self.capacity[2]) + (disk-1) + f_state)

    def get_tot_states(self):
        tot_states = int((self.capacity[0] * self.capacity[1] * self.capacity[2]) +
                (self.capacity[1]*self.capacity[2]) + self.capacity[2])
        if self.f_cpu != math.inf:
            f_states = int((self.f_capacity[0] * self.f_capacity[1] *
                self.f_capacity[2]) + (self.f_capacity[1]*self.f_capacity[2]) +
                self.f_capacity[2])
            tot_states += f_states
        return tot_states

    # TODO: refactor function to work with limited federation resources
    def state_to_capacity(self, state):
        state = int(state+1)
        cpu = divmod(state, int((self.capacity[1]*self.capacity[2])))
        if cpu[0]<=self.capacity[0]:
            value_cpu = cpu[0]
        else:
            value_cpu = self.capacity[0]
        state = int(state-(value_cpu*self.capacity[1]*self.capacity[2]))
        if state == 0:
            value_memory = 0
            value_disk = 0
        else:
            memory = divmod(int(state), int(self.capacity[2]))
            if memory[0]<=self.capacity[1]:
                value_memory = memory[0]
            else:
                value_memory = self.capacity[1]
            state = int(state - (value_memory*self.capacity[2]))
            if state == 0:
                value_disk = 0
            else:
                value_disk = int(state)
        return [value_cpu, value_memory, value_disk]

    def print_status(self):
        print("Environment status:\n")
        print("\tCPU: " + str(self.cpu))
        print("\tDisk: " + str(self.disk))
        print("\tMemory: " + str(self.memory))
        print("\tTime: " + str(self.time) + " seconds")
        print("\tProfit: " + str(self.profit))
        print("\tNumber of Services: "+ str(len(self.service_length)))


    def totalCapacity(self):
        print("Environment capacity:\n ")
        print("\tCPU: " + str(self.capacity[0]))
        print("\tDisk: " + str(self.capacity[1]))
        print("\tMemory: " + str(self.capacity[2]))

        if self.f_cpu != math.inf:
            print("Environment federation capacity:\n ")
            print("\tCPU: " + str(self.f_capacity[0]))
            print("\tDisk: " + str(self.f_capacity[1]))
            print("\tMemory: " + str(self.f_capacity[2]))

    def update_domain(self, current_time):
        self.time = current_time
        if self.total_num_services > 0:
            for i in range((len(self.service_arrival_time)-1), -1, -1):

                if float(current_time) > (float(self.service_arrival_time[i]) + float(self.service_length[i])):
                    self.cpu += float(self.service_cpu[i])
                    self.disk += float(self.service_disk[i])
                    self.memory += float(self.service_memory[i])
                    self.total_num_services -= 1
                    del self.service_cpu[i]
                    del self.service_memory[i]
                    del self.service_disk[i]
                    del self.service_arrival_time[i]
                    del self.service_length[i]

            for j in range((len(self.federated_service_arrival)-1), -1, -1):
                if float(current_time) > (float(self.federated_service_arrival[j]) + float(self.federated_service_length[j])):
                    self.total_num_services -= 1
                    self.f_cpu += float(self.federated_service_cpu[j])
                    self.f_disk += float(self.federated_service_disk[j])
                    self.f_memory += float(self.federated_service_memory[j])
                    del self.federated_service_cpu[j]
                    del self.federated_service_memory[j]
                    del self.federated_service_disk[j]
                    del self.federated_service_length[j]
                    del self.federated_service_arrival[j]

            return int(self.calculate_state()), float(self.profit), self.total_num_services
        else:
            return int(0), float(self.profit), self.total_num_services


    def enough_resources(self, asked_cpu, asked_mem, asked_disk):
        return self.cpu >= asked_cpu and self.memory >= asked_mem and\
                self.disk >= asked_disk

    def enough_federated_resources(self, asked_cpu, asked_mem, asked_disk):
        return self.f_cpu >= asked_cpu and self.f_memory >= asked_mem and\
                self.f_disk >= asked_disk

    def action_profit(self, action, service_cpu, service_memory, service_disk,
                      service_profit, arrival_time, service_length,
                      federate=True):
        # reject
        if action == 2:
            return -service_profit
        # FEDERATION
        elif action == 1 and not federate:
            return -math.inf
        elif action == 1 and  float(self.time) <= float(arrival_time) and\
                    self.enough_federated_resources(service_cpu, service_memory,
                        service_disk):
                return 1
        # local deploy
        else:
            if action == 0 and self.enough_resources(service_cpu,
                    service_memory, service_disk):
                return service_profit
            else:
                return -math.inf

    def instantiate_service(self, action, service_cpu, service_memory, service_disk, service_profit, arrival_time, service_length):
        if action == 2:
            # rejection
            self.profit -= service_profit
            return [self.cpu, self.memory, self.disk, -(service_profit)]
        elif action == 1:
            # FEDERATION
            if float(self.time) <= float(arrival_time) and\
                    self.enough_federated_resources(service_cpu, service_memory,
                        service_disk):

                self.f_cpu -= service_cpu
                self.f_memory -= service_memory
                self.f_disk -= service_disk
                self.federated_service_cpu.append(service_cpu)
                self.federated_service_memory.append(service_memory)
                self.federated_service_disk.append(service_disk)
                self.federated_service_arrival.append(arrival_time)
                self.federated_service_length.append(service_length)

                self.total_num_services += 1

                now_profit = 1
                self.profit += now_profit
                self.total_num_services += 1
                return [self.cpu, self.memory, self.disk, now_profit]
            else: # not enough federation resources => reject
                self.profit -= service_profit
                return [self.cpu, self.memory, self.disk, -(service_profit)]
        else:
            if self.cpu >= service_cpu and self.memory >= service_memory and self.disk >= service_disk \
                    and float(self.time) <= float(arrival_time):
                self.cpu -= service_cpu
                self.memory -= service_memory
                self.disk -= service_disk
                self.profit += service_profit
                self.service_cpu.append(service_cpu)
                self.service_memory.append(service_memory)
                self.service_disk.append(service_disk)
                self.service_arrival_time.append(arrival_time)
                self.service_length.append(service_length)
                self.total_num_services += 1
                # print("New service added")
                return [self.cpu, self.memory, self.disk, service_profit]
            else:
                # TODO: reflect outside that chosen action was to 'federate'
                #print("federate!")
                now_profit = 1
                self.profit += now_profit
                return [self.cpu, self.memory, self.disk, now_profit]

    def get_num_services(self):
        return int(len(self.service_length))

    def get_cpu(self):
        return self.cpu

    def get_memory(self):
        return self.memory

    def get_disk(self):
        return self.disk

    def get_profit(self):
        return float(self.profit)

    def get_fed_capacities(self):
        return self.f_capacity


