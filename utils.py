from imp import find_module, load_source, new_module, PY_SOURCE
import inspect, json

class BaseSolution():
	IN_DIR = 'in/'
	DATA_DIR = 'data/'
	DATA_FILE = 'data.json'

	def __init__(self):
		self.load_data()

	'''
	loads the data from data/data.json 
	'''
	@classmethod
	def load_data(cls):
		submission_data = cls.DATA_DIR + cls.DATA_FILE
		with open(submission_data) as data_file: 
			cls.data = json.load(data_file)

	'''
	load
	takes a file name (sans extension) as input and returns a module
	'''
	def load_py(self, name):
		# print('loading {!s} and creating module . . .\n'.format(name))
		submission_file = self.IN_DIR + str(name)
		fileobj, path, description = find_module(submission_file)

		#throw an error if this isn't a .py file
		if description[2] != PY_SOURCE:
			raise ImportError("no python source file found")
			results = 'FAILURE: file name {!s} given failed to import; no .py source file found'.format(name)

		results = 'SUCCESS: {!s} was successfully imported and returned as a module'.format(name)

		code = compile(fileobj.read(), path, "exec")
		module = new_module(submission_file)
		# sys.modules[name] = module
		exec(code, module.__dict__)
		return module, results


	# '''
	# load a file from the file name and extension
	# potentially a problem as the module name needs to be unique
	# http://blog.thekondor.net/2011/05/python-imploadsource-trap.html
	# '''
	# def load_file(self, file_name):
	# 	print('loading a module from file: {!s}\n'.format(file_name))
	# 	submission_path = self.IN_DIR + str(file_name)
	# 	mod = load_source(file_name, submission_path)
	# 	return mod


	'''
	listFunctionNames takes a module and returns an array of the function names (strings)
	'''	
	@staticmethod
	def listFunctionNames(module):
		all_functions = inspect.getmembers(module, inspect.isfunction)
		names = [x[0] for x in all_functions]
		# if (isinstance(const, type(code)))
		return names


	'''
	listFunctionNames takes a module and returns an array of the function names (strings)
	'''	
	@staticmethod
	def listClassNames(module):
		all_classes = inspect.getmembers(module, inspect.isclass)
		names = [x[0] for x in all_classes]
		# if (isinstance(const, type(code)))
		return names


	'''
	listMethodNames takes a module and returns an array of the method names (strings)
	'''	
	@staticmethod
	def listMethodNames(module):
		all_methods = inspect.getmembers(module, inspect.ismethod)
		names = [x[0] for x in all_methods]
		# if (isinstance(const, type(code)))
		return names


	'''
	checkForFunctions: takes a module and an array of function names (strings), and checks 
	to see if each one exists
	'''	
	# @classmethod
	def checkForFunctions(self, module, expected):
		results = ''
		common_functions = []
		func_names = self.listFunctionNames(module)
		results += "Functions Found: {!s}\n".format(func_names)
		for function in expected:
			if function in func_names:
				results += "PASS: {!s} is defined as a function in {!s}\n".format(function, module.__name__)
				common_functions.append(function)
			else:
				results += "FAIL: {!s} was not defined as a function in {!s}\n".format(function, module.__name__)
		summary = "{!r}/{!r} PASSED\n".format(len(common_functions), len(expected))
		results += summary
		return results, common_functions

	'''
	checkForMethods: given a module and an array of expected methods, returns a string of which methods
	were found in the module and the list of expected methods (this is not working yet, need to cooperate with classes)
	'''
	# @classmethod
	def checkForMethods(self, module, expected):
		results = ''
		common_methods = []
		method_names = self.listMethodNames(module)
		results += "Methods Found: {!s}\n".format(method_names)
		for method in expected:
			if method in method_names:
				results+= "PASS: {!s} is defined as a method in {!s}\n".format(method, module.__name__)
				common_methods.append(method)
			else:
				results+= "FAIL: {!s} was not defined as a method in {!s}\n".format(method, module.__name__)
		summary = "{!r}/{!r} PASSED".format(len(common_methods), len(expected))
		results += summary

		return results, common_methods

	'''
	checkForClasses: given a module and an array of expected classes, returns a string of which classes
	were found in the module and the list of classes
	'''
	def checkForClasses(self, module, expected):
		results = ''
		common_classes = []
		class_names = self.listClassNames(module)
		results += "Classes Found: {!s}\n".format(class_names)
		for cls in expected:
			if cls in class_names:
				results+= "PASS: {!s} is defined as a class in {!s}\n".format(cls, module.__name__)
				common_classes.append(cls)
			else:
				results+= "FAIL: {!s} was not defined as a class in {!s}\n".format(cls, module.__name__)
		summary = "{!r}/{!r} PASSED".format(len(common_classes), len(expected))
		results += summary

		return results, common_classes

	'''
	getAttempts() returns the number of attempts that have been made on this problem
	'''
	@classmethod
	def getAttempts(cls):
		attempts = cls.data['attempts']
		return attempts

		'''
	getTimeDelta() returns the time difference for this problem (right now, -1 = late, 0 = on time)
	'''
	@classmethod
	def getTimeDelta(cls):
		timedelta = cls.data['timedelta']
		return timedelta
