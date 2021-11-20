import pandas as pd
import numpy as np

class VirtualMemory(object):
    def __init__(self):
        self.globalInts = pd.DataFrame(data = np.nan, index = np.arange(0, 3000), columns = ['mem_dir'])
        self.globalFloats = pd.DataFrame(data = np.nan, index = np.arange(3001, 6000), columns = ['mem_dir'])
        self.globalStrings = pd.DataFrame(data = np.nan, index = np.arange(6001, 9000), columns = ['mem_dir'])

        self.localInts = pd.DataFrame(data = np.nan, index = np.arange(9001, 12000), columns = ['mem_dir'])
        self.localFloats = pd.DataFrame(data = np.nan, index = np.arange(12000, 15000), columns = ['mem_dir'])
        self.localStrings = pd.DataFrame(data = np.nan, index = np.arange(15001, 18000), columns = ['mem_dir'])

        self.cteInts = pd.DataFrame(data = np.nan, index = np.arange(18001, 21000), columns = ['mem_dir'])
        self.cteFloats = pd.DataFrame(data = np.nan, index = np.arange(21001, 24000), columns = ['mem_dir'])
        self.cteStrings = pd.DataFrame(data = np.nan, index = np.arange(24001, 27000), columns = ['mem_dir'])

        self.tempInts = pd.DataFrame(data = np.nan, index = np.arange(27001, 30000), columns = ['mem_dir'])
        self.tempFloats = pd.DataFrame(data = np.nan, index = np.arange(30001, 33000), columns = ['mem_dir'])
        self.tempStrings = pd.DataFrame(data = np.nan, index = np.arange(36001, 39000), columns = ['mem_dir'])
        self.tempBools = pd.DataFrame(data = np.nan, index = np.arange(42001, 45000), columns = ['mem_dir'])

    def cteAssign(self, value):
        vType = type(value)

        if vType == int:
            index = self.tempInts.loc[self.tempInts.loc[pd.isnull(self.tempInts.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempInts.loc[index] = value
            return index
        elif vType == float:
            index = self.tempFloats.loc[self.tempFloats.loc[pd.isnull(self.tempFloats.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempFloats.loc[index] = value
            return index
        elif vType == bool:
            index = self.tempBools.loc[self.tempBools.loc[pd.isnull(self.tempBools.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempBools.loc[index] = value
            return index
        else:
            index = self.tempStrings.loc[self.tempStrings.loc[pd.isnull(self.tempStrings.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempStrings.loc[index] = value
            return index

    def temporalAssign(self, vType):
        if vType == int:
            index = self.tempInts.loc[self.tempInts.loc[pd.isnull(self.tempInts.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempInts.loc[index] = "None"
            return index
        elif vType == float:
            index = self.tempFloats.loc[self.tempFloats.loc[pd.isnull(self.tempFloats.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempFloats.loc[index] = "None"
            return index
        elif vType == bool:
            index = self.tempBools.loc[self.tempBools.loc[pd.isnull(self.tempBools.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempBools.loc[index] = "None"
            return index
        else:
            index = self.tempStrings.loc[self.tempStrings.loc[pd.isnull(self.tempStrings.mem_dir)].head(1).index, 'mem_dir'].index
            self.tempStrings.loc[index] = "None"
            return index

    def assignVirtualDirection(self, scope, vType):
        if scope == 'global':
            if vType == int:
                index = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalInts.loc[index] = "None"
                return index
            elif vType == float:
                index = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalFloats.loc[index] = "None"
                return index
            else:
                index = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalStrings.loc[index] = "None"
                return index
        elif scope == 'local':
            if vType == int:
                index = self.localInts.loc[self.localInts.loc[pd.isnull(self.localInts.mem_dir)].head(1).index, 'mem_dir'].index
                self.localInts.loc[index] = "None"
                return index
            elif vType == float:
                index = self.localFloats.loc[self.localFloats.loc[pd.isnull(self.localFloats.mem_dir)].head(1).index, 'mem_dir'].index
                self.localFloats.loc[index] = "None"
                return index
            else:
                index = self.localStrings.loc[self.localStrings.loc[pd.isnull(self.localStrings.mem_dir)].head(1).index, 'mem_dir'].index
                self.localStrings.loc[index] = "None"
                return index