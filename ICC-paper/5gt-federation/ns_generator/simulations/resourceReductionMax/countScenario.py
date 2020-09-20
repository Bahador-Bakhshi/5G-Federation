import json
import os

absPath = os.path.abspath(os.path.dirname(__file__))
configPath = '/'.join(absPath.split('/')[:-2]) + '/simulation-configs'

if __name__ == '__main__':
    mdPath = configPath + '/resourceReductionMax/multiDomain.json'
    entriesPath = configPath + '/resourceReductionMax/entryPoints.json'
    
    print '=================================='
    print '== Available servers per domain =='
    print '=================================='
    with open(mdPath) as f:
        md = json.load(f)
        hostedDomains = [1 for _ in range(md['domains'])]

        for foreignPods, i in zip(md['foreignPods'], range(md['domains'])):
            domServers = 16

            for foreign in foreignPods.keys():
                hostedDomains[int(foreign)] += 1
                domServers += len(foreignPods[foreign]) * 4
            print 'domain ' + str(i) + ' has ' + str(domServers) + ' servers'

        
        print '\n==============================='
        print '== Hosted domains (and itself) =='
        print '================================='
        for hostedDomain, domain in zip(hostedDomains, range(md['domains'])):
            print 'domain ' + str(domain) + ' hosts (with itself) ' +\
                str(hostedDomain) + ' domains'

    
    print '\n============================'
    print '== NS requests per domain =='
    print '============================'

    with open(entriesPath) as f:
        entries = json.load(f)
        domainEntries = [0 for _ in range(md['domains'])]
        
        for entry in entries:
            domainEntries[entry['domain']] += 1

        for domEn, dom in zip(domainEntries, range(md['domains'])):
            print 'domain ' + str(dom) + ' has ' + str(domEn) + ' NS requests'

