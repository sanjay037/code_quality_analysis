from cfg import *
class StaticAnalyser():
	def __init__(self, file_name):
		self.ast = parse_file(file_name, use_cpp = True)
		self.cfg = Cfg(self.ast)
	def cyclomatic_complexity(self):
		self.cfg.print_cyclomatic_complexity()
if(__name__ == "__main__"):
	file_name = raw_input("Enter the filename to be analysed:")
	analyser = StaticAnalyser(file_name)
	analyser.cyclomatic_complexity()
