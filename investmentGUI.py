"""
Program: investmentGUI.py
Author: Robert 4/21/2021

*** Note: The file breezypythongui MUST be in the same directory as this file for the application to work.***
"""
from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstates the use of a multi-line text area widget."""


	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self)
		self.addLabel(text = "initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)

		self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 15)

		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

	# Event handling method.
	def compute(self):
		""" Computes the investment schedule based on the inputs and outputs the schedule."""
		# Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
			return

		# Convert the rate ro a decimal number
		rate = rate / 100

		# intitialize the accumulator for the interest
		totalInterest = 0.0

		# Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", " Interest", "Ending Balance")

		# Compute and append the results for each year
		totalInterest = 0.0
		for year in range(1, years + 1):
			Interest = startBalance * rate
			endBalance = startBalance + Interest
			result += "%4d%18.2f%10.2f%16.2f\n" % \
					  (year, startBalance, Interest, endBalance)
			startBalance = endBalance
			totalInterest += Interest

		# Append the totals for the period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		# Output the result while preserving read-onlt status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"


# Definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	TextAreaDemo().mainloop()

# Global call to the main() function
main()