import json
import os

absPath = os.path.abspath(os.path.dirname(__file__))
configPath = '/'.join(absPath.split('/')[:-2]) + '/simulation-configs'

if __name__ == '__main__':
    with open(configPath + '/resourceReductionMax/multiDomain.json') as f:
        mdCfg = json.load(f)
        print 'disk: ' + str(mdCfg['servRes']['disk']['max'])
        print 'cpu: ' + str(mdCfg['servRes']['cpu']['max'])
        print 'memory: ' + str(mdCfg['servRes']['memory']['max'])
        print 'fatBw: ' + str(mdCfg['fatLnkRes']['bw']['max'])
        print 'meshBw: ' + str(mdCfg['meshLnkRes']['bw']['max'])

