import json
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
			self.cteDirections.loc[index] = value
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

	def getFinalVM(self):
		finalVM = {}
		finalVM["globalInts"] = self.globalInts.to_json()
		finalVM["globalFloats"] = self.globalFloats.to_json()
		finalVM["globalStrings"] = self.globalStrings.to_json()
		finalVM["localInts"] = self.localInts.to_json()
		finalVM["localFloats"] = self.localFloats.to_json()
		finalVM["localStrings"] = self.localStrings.to_json()
		finalVM["cteInts"] = self.cteInts.to_json()
		finalVM["cteFloats"] = self.cteFloats.to_json()
		finalVM["cteStrings"] = self.cteStrings.to_json()
		finalVM["cteDirections"] = self.cteDirections.to_json()
		finalVM["tempInts"] = self.tempInts.to_json()
		finalVM["tempFloats"] = self.tempFloats.to_json()
		finalVM["tempStrings"] = self.tempStrings.to_json()
		finalVM["tempBools"] = self.tempBools.to_json()


		return finalVM
	
	def restoreVM(self, data):
		self.globalInts = json.loads(data["globalInts"])
		self.globalFloats = json.loads(data["globalFloats"])
		self.globalStrings = json.loads(data["globalStrings"])
		self.localInts = json.loads(data["localInts"])
		self.localFloats = json.loads(data["localFloats"])
		self.localStrings = json.loads(data["localStrings"])
		self.cteInts = json.loads(data["cteInts"])
		self.cteFloats = json.loads(data["cteFloats"])
		self.cteStrings = json.loads(data["cteStrings"])
		self.cteDirections = json.loads(data["cteDirections"])
		self.tempInts = json.loads(data["tempInts"])
		self.tempFloats = json.loads(data["tempFloats"])
		self.tempStrings = json.loads(data["tempStrings"])
		self.tempBools = json.loads(data["tempBools"])