import json
import os
import sys

absPath = os.path.abspath(os.path.dirname(__file__))
configPath = '/'.join(absPath.split('/')[:-2]) + '/simulation-configs'

if __name__ == '__main__':
    # argv[1] = disk
    # argv[2] = cpu
    # argv[3] = mem
    # [argv[4] = fatBw]
    # [argv[5] = meshBw]

    mdCfg = None

    with open(configPath + '/tabuPerfectionReduce/multiDomain.json') as f:
        mdCfg = json.load(f)
        f.close()

    mdCfg['servRes']['disk']['max'] = int(float(sys.argv[1]))
    mdCfg['servRes']['disk']['min'] = int(float(sys.argv[1]))

    mdCfg['servRes']['cpu']['max'] = int(float(sys.argv[2]))
    mdCfg['servRes']['cpu']['min'] = int(float(sys.argv[2]))

    mdCfg['servRes']['memory']['max'] = int(float(sys.argv[3]))
    mdCfg['servRes']['memory']['min'] = int(float(sys.argv[3]))

    if len(sys.argv) > 4:
        mdCfg['fatLnkRes']['bw']['max'] = int(float(sys.argv[4]))
        mdCfg['fatLnkRes']['bw']['min'] = int(float(sys.argv[4]))

        mdCfg['meshLnkRes']['bw']['max'] = int(float(sys.argv[5]))
        mdCfg['meshLnkRes']['bw']['min'] = int(float(sys.argv[5]))

    with open(configPath + '/tabuPerfectionReduce/multiDomain.json', 'w') as f:
        json.dump(mdCfg, f)
        f.close()

