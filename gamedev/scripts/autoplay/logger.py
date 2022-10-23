import sys

class Logger:
	def __init__(self) -> None:
		self.log_data: list[str] = []
		self.indent_level = 0
	
	def log(self, msg: str) -> None:
		indent_string: str = "  " * self.indent_level
		indented_msg = f"{indent_string}{msg}"
		self.log0(indented_msg)
	
	# Log with no indentation.
	def log0(self, msg: str) -> None:
		self.log_data.append(msg)
		print(msg)
	
	def indent(self, n:int) -> None:
		self.indent_level += n

	def error(self, msg: str) -> None:
		self.log(msg)
		sys.exit()
