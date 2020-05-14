import random as rand

#Filename to read edge list
inFilename = "EdgeList.txt"
outFilename = "at_t_topology.txt"

#Below dictionary represents min and max value of parameters which needs to be configured
#Key should be alphabatically sorted
parameters = {
    'AR': {
        'delay': {'min': 100, 'max': 1000},
        'bandwidth': {'min': 100, 'max': 1000},
        'metric': 1,
        'queue': {'min': 100, 'max': 1000},
    },
    'RR': {
        'delay': {'min': 100, 'max': 1000},
        'bandwidth': {'min': 100, 'max': 1000},
        'metric': 1,
        'queue': {'min': 100, 'max': 1000},
    },
    'CR': {
        'delay': {'min': 100, 'max': 1000},
        'bandwidth': {'min': 100, 'max': 1000},
        'metric': 1,
        'queue': {'min': 100, 'max': 1000},
    },
    'PR': {
        'delay': {'min': 100, 'max': 1000},
        'bandwidth': {'min': 100, 'max': 1000},
        'metric': 1,
        'queue': {'min': 100, 'max': 1000},
    },
}


def main():
    file = open(inFilename, 'r')
    outFile = open(outFilename, 'w')

    nodeNames = {}
    outLines = []

    for line in file:
        words = line.split()
        words = sorted(words)
        key = words[0][0] + words[1][0]
        outline = "{0}\t{1}\t{2}bps\t{3}\t{4}\n".format(
            words[0], words[1],
            rand.randrange(parameters[key]['bandwidth']['min'], parameters[key]['bandwidth']['max']),
            parameters[key]['metric'],
            rand.randrange(parameters[key]['delay']['min'], parameters[key]['delay']['max']),
            rand.randrange(parameters[key]['queue']['min'], parameters[key]['queue']['max'])
        )
        outLines.append(outline)

        nodeNames[words[0]] = 1
        nodeNames[words[1]] = 1

    nodeNames = [key + '\tNA\t 0\t0\n' for key in nodeNames.keys()]
    nodeNames.insert(0, "# node\tcomment\tyPos\txPos\n")
    outLines.insert(0, "# srcNode\tdstNode\tbandwidth\tmetric\tdelay\tqueue\n")
    outLines = nodeNames + outLines

    outFile.writelines(outLines)

    outFile.close()
    file.close()


main()