'''
6.5.15
_solution.py tests main.py 
'''

from base import BaseSolution

EXPECTED_FUNCTIONS = ['count', 'square']


# get the module of the file we want to test
# (can alternatively use solution.load_file(<filename.py>))
# main_module = solution.load('main')

#list the available functions in this module 
# main_module_functions = solution.listFunctionNames(main_module)

#test to see if the expected functions exist in the module
# for function in EXPECTED_FUNCTIONS:
# 	if function in main_module_functions:
# 		print("PASS: {!s} is defined as a function in main_module".format(function))
# 	else:
# 		print("FAIL: {!s} was not defined as a function in main_module".format(function))

# solution.checkFunctions(main_module, EXPECTED_FUNCTIONS)

class TestSolution(BaseSolution):
	def __init__(self, submission_file):
		self.module = self.load(submission_file)
		self.output = []

	'''
	load
	takes a file name (sans extension) as input and returns a module
	'''
	# def load(self, name):
	# 	print('loading {!s} and creating module'.format(name))
	# 	submission_file = self.IN_DIR + str(name)
	# 	fileobj, path, description = find_module(submission_file)

	# 	#throw an error if this isn't a .py file
	# 	if description[2] != PY_SOURCE:
	# 		raise ImportError("no python source file found")

	# 	code = compile(fileobj.read(), path, "exec")
	# 	module = new_module(submission_file)
	# 	# sys.modules[name] = module
	# 	exec(code, module.__dict__)
	# 	return module


	def set_expected_functions(self, function_list):
		summary = "\nSETTING expected functions for module {!s} to {!s}".format(self.module.__name__, function_list)
		# print(summary)
		self.output.append(summary)
		self.expected_functions = function_list

	def set_expected_methods(self, method_list):
		summary = "\nSETTING expected methods for module {!s} to {!s}".format(self.module.__name__, method_list)
		# print(summary)
		self.output.append(summary)
		self.expected_methods = method_list

	def set_expected_classes(self, method_list):
		summary = "\nSETTING expected classes for module {!s} to {!s}".format(self.module.__name__, class_list)
		# print(summary)
		self.output.append(summary)
		self.expected_classes = class_list

	def check_expected_functions(self):
		summary = "\nCHECKING expected functions for module {!s}:".format(self.module.__name__)
		# print(summary)
		self.output.append(summary)
		self.output.append(self.checkForFunctions(self.module, self.expected_functions))

	def check_expected_methods(self):
		summary = "\nCHECKING expected methods for module {!s}:".format(self.module.__name__)
		# print(summary)
		self.output.append(summary)
		self.output.append(self.checkForMethods(self.module, self.expected_methods))

	def check_expected_classes(self):
		summary = "\nCHECKING expected classes for module {!s}:".format(self.module.__name__)
		# print(summary)
		self.output.append(summary)
		self.output.append(self.checkForClasses(self.module, self.expected_classes))

	def run_function(self, function_name):
		func = getattr(self.module, function_name)
		func(2)

	'''
	returns the number of arguments a given function
	'''
	def get_function_args(self, function_name):
		f = getattr(self.module, function_name)
		summary = "\nCHECKING function argument num for module {!s}:".format(self.module.__name__)
		arg_count = f.__code__.co_argcount
		print(arg_count)

	def report(self):
		return self.output



mainTest = TestSolution('main')
mainTest.set_expected_functions(['count', 'square'])
mainTest.check_expected_functions()

mainTest.set_expected_methods(['count', 'square'])
mainTest.check_expected_methods()

mainTest.get_function_attrs('count')
report = mainTest.report()

for subreport in report:
	print(subreport)
# mainTest.run_function('count')
