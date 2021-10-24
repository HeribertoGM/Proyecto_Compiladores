import pandas as pd
import numpy as np

class VirtualMachine(object):
    def __init__(self):
        self.globalInts = pd.DataFrame(data = np.nan, index = np.arange(0, 1000), columns = ['mem_dir'])
        self.globalFloats = pd.DataFrame(data = np.nan, index = np.arange(1001, 2000), columns = ['mem_dir'])
        self.globalStrings = pd.DataFrame(data = np.nan, index = np.arange(2001, 3000), columns = ['mem_dir'])

        self.localInts = pd.DataFrame(data = np.nan, index = np.arange(3001, 4000), columns = ['mem_dir'])
        self.localFloats = pd.DataFrame(data = np.nan, index = np.arange(4001, 5000), columns = ['mem_dir'])
        self.localStrings = pd.DataFrame(data = np.nan, index = np.arange(5001, 6000), columns = ['mem_dir'])

        self.cteInts = pd.DataFrame(data = np.nan, index = np.arange(6001, 7000), columns = ['mem_dir'])
        self.cteFloats = pd.DataFrame(data = np.nan, index = np.arange(7001, 8000), columns = ['mem_dir'])
        self.cteStrings = pd.DataFrame(data = np.nan, index = np.arange(8001, 9000), columns = ['mem_dir'])

        self.tempInts = pd.DataFrame(data = np.nan, index = np.arange(9001, 10000), columns = ['mem_dir'])
        self.tempFloats = pd.DataFrame(data = np.nan, index = np.arange(10001, 11000), columns = ['mem_dir'])
        self.tempStrings = pd.DataFrame(data = np.nan, index = np.arange(11001, 12000), columns = ['mem_dir'])
        self.tempBools = pd.DataFrame(data = np.nan, index = np.arange(12001, 13000), columns = ['mem_dir'])

    def assignVirtualDirection(self, scope, vType):
        if scope == 'global':
            if vType == int:
                index = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalInts.loc[index] = 0
                return index
            elif vType == float:
                index = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalFloats.loc[index] = 0
                return index
            else:
                index = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
                self.globalStrings.loc[index] = 0
                return index
        # elif scope == 'local':
        #     if vType == int:
        #         index = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
        #         # self.globalInts.loc[index] = value
        #         return index
        #     elif vType == float:
        #         index = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
        #         # self.globalFloats.loc[index] = value
        #         return index
        #     else:
        #         index = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
        #         # self.globalStrings.loc[index] = value
        #         return index