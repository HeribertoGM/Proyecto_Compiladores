import json
import sys
import pandas as pd
import numpy as np

class VirtualMemory(object):
	def __init__(self):
		self.globalInts = pd.DataFrame(data = np.nan, index = np.arange(0, 3000), columns = ['mem_dir'])
		self.globalFloats = pd.DataFrame(data = np.nan, index = np.arange(3001, 6000), columns = ['mem_dir'])
		self.globalStrings = pd.DataFrame(data = np.nan, index = np.arange(6001, 9000), columns = ['mem_dir'])

		self.localInts = pd.DataFrame(data = np.nan, index = np.arange(9001, 12000), columns = ['mem_dir'])
		self.localFloats = pd.DataFrame(data = np.nan, index = np.arange(12001, 15000), columns = ['mem_dir'])
		self.localStrings = pd.DataFrame(data = np.nan, index = np.arange(15001, 18000), columns = ['mem_dir'])

		self.cteInts = pd.DataFrame(data = np.nan, index = np.arange(18001, 21000), columns = ['mem_dir'])
		self.cteFloats = pd.DataFrame(data = np.nan, index = np.arange(21001, 24000), columns = ['mem_dir'])
		self.cteStrings = pd.DataFrame(data = np.nan, index = np.arange(24001, 27000), columns = ['mem_dir'])
		self.cteDirections = pd.DataFrame(data = np.nan, index = np.arange(27001, 30000), columns = ['mem_dir'])

		self.tempInts = pd.DataFrame(data = np.nan, index = np.arange(30001, 33000), columns = ['mem_dir'])
		self.tempFloats = pd.DataFrame(data = np.nan, index = np.arange(33001, 36000), columns = ['mem_dir'])
		self.tempStrings = pd.DataFrame(data = np.nan, index = np.arange(36001, 39000), columns = ['mem_dir'])
		self.tempBools = pd.DataFrame(data = np.nan, index = np.arange(39001, 42000), columns = ['mem_dir'])

	def cteAssign(self, value):
		vType = type(value)

		if vType == int:
			index = self.cteInts.loc[self.cteInts.loc[pd.isnull(self.cteInts.mem_dir)].head(1).index, 'mem_dir'].index
			self.cteInts.loc[index] = value
			return int(index[0])
		elif vType == float:
			index = self.cteFloats.loc[self.cteFloats.loc[pd.isnull(self.cteFloats.mem_dir)].head(1).index, 'mem_dir'].index
			self.cteFloats.loc[index] = value
			return int(index[0])
		elif vType == str:
			index = self.cteStrings.loc[self.cteStrings.loc[pd.isnull(self.cteStrings.mem_dir)].head(1).index, 'mem_dir'].index
			self.cteStrings.loc[index] = value
			return int(index[0])
		else:
			index = self.cteDirections.loc[self.cteDirections.loc[pd.isnull(self.cteDirections.mem_dir)].head(1).index, 'mem_dir'].index
			self.cteDirections.loc[index] = value[0]
			return int(index[0])

	def temporalAssign(self, vType):
		if vType == "int":
			index = self.tempInts.loc[self.tempInts.loc[pd.isnull(self.tempInts.mem_dir)].head(1).index, 'mem_dir'].index
			self.tempInts.loc[index] = "None"
			return int(index[0])
		elif vType == "float":
			index = self.tempFloats.loc[self.tempFloats.loc[pd.isnull(self.tempFloats.mem_dir)].head(1).index, 'mem_dir'].index
			self.tempFloats.loc[index] = "None"
			return int(index[0])
		elif vType == "bool":
			index = self.tempBools.loc[self.tempBools.loc[pd.isnull(self.tempBools.mem_dir)].head(1).index, 'mem_dir'].index
			self.tempBools.loc[index] = "None"
			return int(index[0])
		else:
			index = self.tempStrings.loc[self.tempStrings.loc[pd.isnull(self.tempStrings.mem_dir)].head(1).index, 'mem_dir'].index
			self.tempStrings.loc[index] = "None"
			return int(index[0])

	def assignVirtualDirection(self, scope, vType):
		if scope == 'global':
			if vType == "int":
				index = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalInts.loc[index] = "None"
				return int(index[0])
			elif vType == "float":
				index = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalFloats.loc[index] = "None"
				return int(index[0])
			else:
				index = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalStrings.loc[index] = "None"
				return int(index[0])
		elif scope == 'local':
			if vType == "int":
				index = self.localInts.loc[self.localInts.loc[pd.isnull(self.localInts.mem_dir)].head(1).index, 'mem_dir'].index
				self.localInts.loc[index] = "None"
				return int(index[0])
			elif vType == "float":
				index = self.localFloats.loc[self.localFloats.loc[pd.isnull(self.localFloats.mem_dir)].head(1).index, 'mem_dir'].index
				self.localFloats.loc[index] = "None"
				return int(index[0])
			else:
				index = self.localStrings.loc[self.localStrings.loc[pd.isnull(self.localStrings.mem_dir)].head(1).index, 'mem_dir'].index
				self.localStrings.loc[index] = "None"
				return int(index[0])

	def assignMemoryArray(self, scope, vType, size):
		if scope == 'global':
			if vType == "int":
				index = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalInts.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.globalInts.loc[self.globalInts.loc[pd.isnull(self.globalInts.mem_dir)].head(1).index, 'mem_dir'].index
					self.globalInts.loc[index2] = "None"
				return int(index[0])
			elif vType == "float":
				index = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalFloats.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.globalFloats.loc[self.globalFloats.loc[pd.isnull(self.globalFloats.mem_dir)].head(1).index, 'mem_dir'].index
					self.globalFloats.loc[index2] = "None"
				return int(index[0])
			else:
				index = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
				self.globalStrings.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.globalStrings.loc[self.globalStrings.loc[pd.isnull(self.globalStrings.mem_dir)].head(1).index, 'mem_dir'].index
					self.globalStrings.loc[index2] = "None"
				return int(index[0])
		elif scope == 'local':
			if vType == "int":
				index = self.localInts.loc[self.localInts.loc[pd.isnull(self.localInts.mem_dir)].head(1).index, 'mem_dir'].index
				self.localInts.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.localInts.loc[self.localInts.loc[pd.isnull(self.localInts.mem_dir)].head(1).index, 'mem_dir'].index
					self.localInts.loc[index2] = "None"
				return int(index[0])
			elif vType == "float":
				index = self.localFloats.loc[self.localFloats.loc[pd.isnull(self.localFloats.mem_dir)].head(1).index, 'mem_dir'].index
				self.localFloats.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.localFloats.loc[self.localFloats.loc[pd.isnull(self.localFloats.mem_dir)].head(1).index, 'mem_dir'].index
					self.localFloats.loc[index2] = "None"
				return int(index[0])
			else:
				index = self.localStrings.loc[self.localStrings.loc[pd.isnull(self.localStrings.mem_dir)].head(1).index, 'mem_dir'].index
				self.localStrings.loc[index] = "None"
				for i in range(size - 1):
					index2 = self.localStrings.loc[self.localStrings.loc[pd.isnull(self.localStrings.mem_dir)].head(1).index, 'mem_dir'].index
					self.localStrings.loc[index2] = "None"
				return int(index[0])
	
	def getValueWithIndex(self, index):
		if index >= 0 and index <= 3000:
			return self.globalInts.loc[index]["mem_dir"]
		elif index >= 3001 and index <= 6000:
			return self.globalFloats.loc[index]["mem_dir"]
		elif index >= 6001 and index <= 9000:
			return self.globalStrings.loc[index]["mem_dir"]
		elif index >= 9001 and index <= 12000:
			return self.localInts.loc[index]["mem_dir"]
		elif index >= 12001 and index <= 15000:
			return self.localFloats.loc[index]["mem_dir"]
		elif index >= 15001 and index <= 18000:
			return self.localStrings.loc[index]["mem_dir"]
		elif index >= 18001 and index <= 21000:
			return self.cteInts.loc[index]["mem_dir"]
		elif index >= 21001 and index <= 24000:
			return self.cteFloats.loc[index]["mem_dir"]
		elif index >= 24001 and index <= 27000:
			return self.cteStrings.loc[index]["mem_dir"]
		elif index >= 27001 and index <= 30000:
			return self.cteDirections.loc[index]["mem_dir"]
		elif index >= 30001 and index <= 33000:
			return self.tempInts.loc[index]["mem_dir"]
		elif index >= 33001 and index <= 36000:
			return self.tempFloats.loc[index]["mem_dir"]
		elif index >= 36001 and index <= 39000:
			return self.tempStrings.loc[index]["mem_dir"]
		elif index >= 39001 and index <= 42000:
			return self.tempBools.loc[index]["mem_dir"]
		else:
			print("Index Error - Index out of range")
			sys.exit()

	def setValueWithIndex(self, index, value):
		if index >= 0 and index <= 3000:
			self.globalInts.loc[index] = value
		elif index >= 3001 and index <= 6000:
			self.globalFloats.loc[index] = value
		elif index >= 6001 and index <= 9000:
			self.globalStrings.loc[index] = value
		elif index >= 9001 and index <= 12000:
			self.localInts.loc[index] = value
		elif index >= 12001 and index <= 15000:
			self.localFloats.loc[index] = value
		elif index >= 15001 and index <= 18000:
			self.localStrings.loc[index] = value
		elif index >= 18001 and index <= 21000:
			self.cteInts.loc[index] = value
		elif index >= 21001 and index <= 24000:
			self.cteFloats.loc[index] = value
		elif index >= 24001 and index <= 27000:
			self.cteStrings.loc[index] = value
		elif index >= 27001 and index <= 30000:
			self.cteDirections.loc[index] = value
		elif index >= 30001 and index <= 33000:
			self.tempInts.loc[index] = value
		elif index >= 33001 and index <= 36000:
			self.tempFloats.loc[index] = value
		elif index >= 36001 and index <= 39000:
			self.tempStrings.loc[index] = value
		elif index >= 39001 and index <= 42000:
			self.tempBools.loc[index] = value
		else:
			print("Index Error - Index out of range")
			sys.exit()

	def printTables(self):
			print(self.globalInts.loc[0:10])
			print(self.globalFloats.loc[3001:3010])
			print(self.globalStrings.loc[6001:6010])
			print(self.localInts.loc[9001:9010])
			print(self.localFloats.loc[12001:12010])
			print(self.localStrings.loc[15001:15010])
			print(self.cteInts.loc[18001:18010])
			print(self.cteFloats.loc[21001:21010])
			print(self.cteStrings.loc[24001:24010])
			print(self.cteDirections.loc[27001:27010])
			print(self.tempInts.loc[30001:30010])
			print(self.tempFloats.loc[33001:33010])
			print(self.tempStrings.loc[36001:36010])
			print(self.tempBools.loc[39001:39010])