# 5GT federation simulations
This repository is oriented to perform simulations for federation
interactions in 5G networks.

### Clone with submodule
This repository uses the `vnfs-mapping` submodule to generate the network
service graphs. To clone with the submodule run:
```bash
git clone --recursive https://github.com/MartinPJorge/5gt-federation.git
```

### Dependencies
Following python packages must be installed for code execution:
```bash
pip install networkx==1.9.1
pip install AgglomCluster
```

## NS jukebox
The NS jukebox tool `utils/ns_jukebox.py` randomly generates network service
graphs based on a set of characteristics specified within a configuration file
as the one in `utils/config/nsGenConf.json`.

These are the parameters available in the configuration file:
 * **splits**: number of splits within the NS graph. A split is the point in
   the network service graph where a VNF1 receives traffic only from VNF0, but
   then forwards traffic to VNF2...VNFn;
 * **splitWidth**: number of VNFs after the VNF split, if VNF1 forwards traffic
   towards VNF2, VNF3, VNF4; the split width is equal to 3;
 * **branches**: maximum number of parallel flows within the NS graph;
 * **vnfs**: maximum number of VNFs within the NS graph;
 * **linkTh**: (min,max) values to generate the virtual links characteristics
   below. If `linkTh["traffic"]["min"]=2` and `linkTh["traffic"]["min"]=5`,
   then the algorithm can generate a bandwidth demand between 2 and 5.
   * **linkTh["traffic"]**: (min,max) interval for virtual link bandwidth;
   * **linkTh["delay"]**: (min,max) interval for virtual link bandwidth;
 * **vnfTh**: (min,max) values to generate the VNF characteristics below.
   * **vnfTh["processing-time"]**: VNF processing time required by a VNF;
   * **vnfTh["processing-time"]["cpu"]**: VNF required CPU;
   * **vnfTh["processing-time"]["memory"]**: VNF required memory;
   * **vnfTh["processing-time"]["storage"]**: VNF required disk;

### Execution example
Following example generates 2 NS graphs based on the example configuration
file, and stores the virtual links and VNFs CSVs under `/tmp`:
```bash
$ python ns_jukebox.py config/nsGenConf.json 2 /tmp
Generating 0-th NS for config config/nsGenConf.json
  VNF CSV at: /tmp/vls-0.csv
  VL CSV at: /tmp/vnfs-0.csv
Generating 1-th NS for config config/nsGenConf.json
  VNF CSV at: /tmp/vls-1.csv
  VL CSV at: /tmp/vnfs-1.csv
```

### Output CSV examples
For each generated network service, two files are created. One for the virtual
links:
```csv
delay,traffic,prob,idVNFa,idVNFb
5,502,0.7904173707373455,1,2
2,105,0.20958262926265447,1,3
2,238,1,2,4
3,39,1,3,4
4,712,1,4,5
1,882,1,5,6
2,528,1,6,7
2,767,1,7,8
5,971,1,8,9
4,880,1,9,10
```
and another for the VNFs:
```csv
requirements,processing_time,id,memory,vnf_name,disk,cpu,idVNF
{},3,1,561,v_gen_1_4_1553105587.72,4753,23,1
{},3,2,842,v_gen_2_3_1553105587.72,9639,3,2
{},2,3,997,v_gen_3_2_1553105587.72,9654,9,3
{},19,4,864,v_gen_4_16_1553105587.73,4212,24,4
{},1,5,821,v_gen_5_5_1553105587.73,3482,14,5
{},19,6,219,v_gen_6_1_1553105587.73,8530,9,6
{},15,7,631,v_gen_7_3_1553105587.73,7358,9,7
{},7,8,64,v_gen_8_19_1553105587.73,6339,18,8
{},16,9,91,v_gen_9_3_1553105587.73,7679,14,9
{},8,10,516,v_gen_10_13_1553105587.73,5315,13,10
```


## NS splitter
This script performs the clustering of a network service graph given the
virtual links and VNFs CSV files.

It is executed running:
```bash
python ns_splitter.py /tmp/vnfs-1.csv /tmp/vls-1.csv /tmp
```
where first and second arguments are the VNFs and VLs CSV files generated with
`ns_jukebox.py`, respectively.
And last parameter is the directory where the clusters are stored following
naming convention
`ns-NS_NUM-clusters-NUM_CLUSTERS-clusterCLUSTER_NUM-(vls|vnfs).csv`.
That is, the script tries to create from 1 up to `len(VNF)` clusters, then it
generates CSV files for the VNFs and VLs within each cluster.
```txt
=== 2 CLUSTERS ===
                              | ns-1-clusters-2-cluster0-vnfs.csv
                 __cluster-0__| ns-1-clusters-2-cluster0-vls.csv
                /
vnfs-1.csv |___/
vls-1.csv  |   \              | ns-1-clusters-2-cluster1-vnfs.csv
                \__cluster-1__| ns-1-clusters-2-cluster1-vls.csv

=== 3 CLUSTERS ===
                            
                 __cluster-0__ ...
                /
vnfs-1.csv |___/___cluster-1__ ...
vls-1.csv  |   \            
                \__cluster-2__ ...

[...]

```


#### Acknowledgements
5G-TRANSFORMER Project under Grant 761536. Parts of this paper have
been published in the Proceedings of the IEEE BMSB 2018, Valencia, Spain.
