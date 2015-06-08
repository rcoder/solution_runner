from imp import find_module, load_source, new_module, PY_SOURCE
import inspect

class BaseSolution():
	IN_DIR = 'in/'
	DATA_DIR = 'data/'

	
	'''
	load
	takes a file name (sans extension) as input and returns a module
	'''
	def load(self, name):
		print('loading {!s} and creating module'.format(name))
		submission_file = self.IN_DIR + str(name)
		fileobj, path, description = find_module(submission_file)

		#throw an error if this isn't a .py file
		if description[2] != PY_SOURCE:
			raise ImportError("no python source file found")

		code = compile(fileobj.read(), path, "exec")
		module = new_module(submission_file)
		# sys.modules[name] = module
		exec(code, module.__dict__)
		return module


	'''
	load a file from the file name and extension
	potentially a problem as the module name needs to be unique
	http://blog.thekondor.net/2011/05/python-imploadsource-trap.html
	'''
	def load_file(self, file_name):
		print('loading a module from file: {!s}\n'.format(file_name))
		submission_path = self.IN_DIR + str(file_name)
		mod = load_source(file_name, submission_path)
		return mod


	'''
	listFunctionNames takes a module and returns an array of the function names (strings)
	'''	
	def listFunctionNames(module):
		all_functions = inspect.getmembers(module, inspect.isfunction)
		names = [x[0] for x in all_functions]
		# if (isinstance(const, type(code)))
		return names


	'''
	listFunctionNames takes a module and returns an array of the function names (strings)
	'''	
	def listClassNames(module):
		all_classes = inspect.getmembers(module, inspect.isclass)
		names = [x[0] for x in all_classes]
		# if (isinstance(const, type(code)))
		return names


	'''
	listMethodNames takes a module and returns an array of the method names (strings)
	'''	
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
		count = 0
		func_names = BaseSolution.listFunctionNames(module)
		results += "Functions Found: {!s}\n".format(func_names)
		for function in expected:
			if function in func_names:
				results += "PASS: {!s} is defined as a function in {!s}\n".format(function, module.__name__)
				count += 1
			else:
				results += "FAIL: {!s} was not defined as a function in {!s}\n".format(function, module.__name__)
		summary = "{!r}/{!r} PASSED\n".format(count, len(func_names))
		results += summary
		return results

	# @classmethod
	def checkForMethods(self, module, expected):
		results = ''
		count = 0
		method_names = BaseSolution.listMethodNames(module)
		results += "Methods Found: {!s}\n".format(method_names)
		for method in expected:
			if method in method_names:
				results+= "PASS: {!s} is defined as a method in {!s}\n".format(method, module.__name__)
				count += 1
			else:
				results+= "FAIL: {!s} was not defined as a method in {!s}\n".format(method, module.__name__)
		summary = "{!r}/{!r} PASSED".format(count, len(method_names))
		results += summary

		return results

	def checkForClasses(self, module, expected):
		results = ''
		count = 0
		class_names = BaseSolution.listClassNames(module)
		results += "Classes Found: {!s}\n".format(class_names)
		for cls in expected:
			if cls in class_names:
				results+= "PASS: {!s} is defined as a class in {!s}\n".format(cls, module.__name__)
				count += 1
			else:
				results+= "FAIL: {!s} was defined as a class in {!s}\n".format(cls, module.__name__)
		summary = "{!r}/{!r} PASSED".format(count, len(class_names))
		results += summary

		return results

	def getData():
		#returns a small object with tries and time delta between submission date and due date
		print('returning data')

