'''
6.5.15
_solution.py tests main.py 
'''

from utils import BaseSolution

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
		super().__init__()
		self.module, results = super().load_py(submission_file)
		self.output = [results]

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

	def set_expected_classes(self, class_list):
		summary = "\nSETTING expected classes for module {!s} to {!s}".format(self.module.__name__, class_list)
		# print(summary)
		self.output.append(summary)
		self.expected_classes = class_list

	def check_expected_functions(self):
		summary = "\nCHECKING expected functions for module {!s}:".format(self.module.__name__)
		self.output.append(summary)

		results, common_functions = super().checkForFunctions(self.module, self.expected_functions)
		self.output.append(results)
		return common_functions

	def check_expected_methods(self):
		summary = "\nCHECKING expected methods for module {!s}:".format(self.module.__name__)
		self.output.append(summary)

		results, common_methods = super().checkForMethods(self.module, self.expected_methods)
		self.output.append(results)
		return common_methods

	def check_expected_classes(self):
		summary = "\nCHECKING expected classes for module {!s}:".format(self.module.__name__)
		self.output.append(summary)

		results, common_classes = super().checkForClasses(self.module, self.expected_classes)
		self.output.append(results)
		return common_classes


	'''
	runs a function within the module args[0] should be the function name, 
	args[1..n] get passed to the function in the module
	'''
	def run_function(self, *args):
		#to do: throw an error if this doesn't work
		args = list(args)
		function_name = args[0]
		params = args[1:]
		func = getattr(self.module, function_name)

		summary = "RUNNING {!s} with parameters {!s}\n".format(function_name, *params)
		results = func(*params)
		summary += "RESULTS: {!s}".format(results)


		# potentially also add the output (if any) of the function
		self.output.append(summary)
		return results


	'''
	returns the number of arguments a given function
	'''
	def get_function_args(self, function_name):
		f = getattr(self.module, function_name)
		summary = "\nCHECKING function argument num for module {!s}:".format(self.module.__name__)
		arg_count = f.__code__.co_argcount
		summary += "RESULT: the function {!s} takes {!r} argument(s)".format(function_name, arg_count)
		self.output.append(summary)
		return arg_count

	def get_attempts(self):
		summary = "CHECKING number of attempts\n"
		attempts = super().getAttempts()
		summary += "RESULTS: {!r} attempt(s) have been made".format(attempts)
		self.output.append(summary)
		return attempts

	def report(self):
		return self.output


#create a new solution to main module (loaded from the file in/main.py)
mainTest = TestSolution('main')
mainTest.get_attempts()

#tell the solution to expect these functions in the main module
mainTest.set_expected_functions(['count', 'square'])
mainTest.check_expected_functions()

mainTest.set_expected_methods(['count', 'square'])
mainTest.check_expected_methods()

mainTest.set_expected_classes(['SquareInt'])
mainTest.check_expected_classes()

#we know 'count' exists, we can check how many args it takes if we want
mainTest.get_function_args('count')

#run count() from the main module with a given input (5)
mainTest.run_function('count', 5)

report = mainTest.report()

#print out the reports
for subreport in report:
	print(subreport)
# mainTest.run_function('count')
