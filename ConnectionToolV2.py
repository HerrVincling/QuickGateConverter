import json

# BPJSON()
#   -load/saveJSON
#   -createLogicGate(s)
#   -makeConnection(s)
#   -wireFrames
#   -wireDecoder

class BPJSON():
    def __init__(self):
        self.jsonFile = {"bodies":[{"childs":[]}],"version":3}
        self.childDict = {}
        self.blockCount = 0
        self.connectionCount = 0

    def loadJSON(self, path):
        with open(path, 'r', encoding='utf8') as file:
            data = file.read()
        self.jsonFile = json.loads(data)

    def saveJSON(self, path):
        with open(path, 'w') as file:
            file.write(json.dumps(self.jsonFile, indent=2))

    def createChildDict(self):
        self.childDict = {}
        for child in self.jsonFile['bodies'][0]['childs']:
            self.childDict[child['controller']['id']] = self.jsonFile['bodies'][0]['childs'].index(child)

    def makeConnection(self, ID1, ID2):
        self.jsonFile['bodies'][0]['childs'][self.childDict[ID1]]['controller']['controllers'].append({'id': ID2})
        self.connectionCount += 1

    def makeConnections(self, IDs1, IDs2):
        for i in range(0,len(IDs1)):
            self.jsonFile['bodies'][0]['childs'][self.childDict[IDs1[i]]]['controller']['controllers'].append({'id': IDs2[i]})
            self.connectionCount += 1

    # Mode: 0=AND, 1=OR, 2=XOR, 3=NAND, 4=NOR, 5=XNOR
    def createLogicGate(self, x, y, z, color, id, mode):
        self.jsonFile['bodies'][0]['childs'].append(
            {"color": color, "controller":
                {"active": False, "controllers": [], "id": id, "joints": None, "mode": mode},
             "pos": {"x": x, "y": y, "z": z},
             "shapeId": "9f0f56e8-2c31-4d83-996c-d00a9b296c3f", "xaxis": 1, "zaxis": -2}
        )
        self.blockCount += 1

    # Direction: Vector(x, y, z)
    def createLogicGates(self, x, y, z, direction, color, ids, mode):
        xyz = [x, y, z]
        for id in ids:
            self.createLogicGate(xyz[0], xyz[1], xyz[2], color, id, mode)
            xyz = [xyz[i] + direction[i] for i in range(3)]

    def wireFrames(self, decoderGateIDs, dataGateIDs, data):
        for i in range(len(data)):
            child = self.childDict[decoderGateIDs[i]]
            for j in range(len(dataGateIDs)):
                if data[i][j]:
                    self.jsonFile['bodies'][0]['childs'][child]['controller']['controllers'].append({'id': dataGateIDs[j]})
                    self.connectionCount += 1

    def wireDecoder(self, inputIDs, inputNegIDs, decoderGateIDs):
        for i in range(0, len(inputIDs)):
            for j in range(0, len(decoderGateIDs)):
                if (j) % (2 ** (i + 1)) < (2 ** i):
                    self.makeConnection(inputNegIDs[i], decoderGateIDs[j])
                else:
                    self.makeConnection(inputIDs[i], decoderGateIDs[j])

    def getConnections(self, child):
        return self.jsonFile['bodies'][0]['childs'][child]['controller']['controllers']

    def getCoordinates(self, childs):
        results = []
        for i in childs:
            results.append(self.jsonFile['bodies'][0]['childs'][i]['pos'])
        return results
