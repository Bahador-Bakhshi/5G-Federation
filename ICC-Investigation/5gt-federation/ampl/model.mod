set timestamps ordered;

param profit_federate {timestamps};
param profit_local {timestamps};
param profit_reject {timestamps};
param asked_cpu {timestamps};
param asked_mem {timestamps};
param asked_disk {timestamps};
param frees_cpu {timestamps};
param frees_mem {timestamps};
param frees_disk {timestamps};
param frees_arrival {timestamps}; # Arrival timestamp of leaving
                                  # service

var federate {timestamps} binary;
var local {timestamps} binary;
var reject {timestamps} binary;
var cpu {timestamps};
var mem {timestamps};
var disk {timestamps};

subject to match_cpu {t in timestamps: first(timestamps) <> t}:
        cpu[t] = cpu[prev(t)] - local[prev(t)]*asked_cpu[prev(t)]
            + local[frees_arrival[prev(t)]]*frees_cpu[prev(t)];
subject to match_mem {t in timestamps: first(timestamps) <> t}:
        mem[t] = mem[prev(t)] - local[prev(t)]*asked_mem[prev(t)]
            + local[frees_arrival[prev(t)]]*frees_mem[prev(t)];
subject to match_disk {t in timestamps: first(timestamps) <> t}:
        disk[t] = disk[prev(t)] - local[prev(t)]*asked_disk[prev(t)]
            + local[frees_arrival[prev(t)]]*frees_disk[prev(t)];

subject to choose_one_option {t in timestamps}:
    federate[t] + local[t] + reject[t] = 1;

subject to no_cpu_runout {t in timestamps}:
    cpu[t] >= 0;
subject to no_mem_runout {t in timestamps}:
    mem[t] >= 0;
subject to no_disk_runout {t in timestamps}:
    disk[t] >= 0;

maximize total_profit:
    sum {t in timestamps} (profit_federate[t] * federate[t] +
        profit_local[t] * local[t] +
        profit_reject[t] * reject[t]);

