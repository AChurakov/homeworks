def reverse_polish_notation_calc(expr):
	try:
		OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
		stack = []
		for token in expr.split(" "):
			if token in OPERATORS:
				op2, op1 = stack.pop(), stack.pop()
				stack.append(OPERATORS[token](op1,op2))
			elif token:
				stack.append(float(token))

		return stack.pop() if len(stack) == 1 else 'ERROR'

	except:
		return 'ERROR'

print(reverse_polish_notation_calc(input()))