def arithmetic_arranger(problems, show_answers=False):
    """
    Arrange arithmetic problems vertically and optionally display results.

    Parameters:
    - problems: list of strings, each a simple arithmetic problem
    - show_answers: bool, whether to include the results in the output

    Returns:
    - A formatted string of the arranged problems or an error message.
    """
    
    first_line = []
    second_line = []
    dash_line = []
    total_line = []
    
    # Validate the number of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        # Validate operator
        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Extract and clean operands
        a, b = map(str.strip, problem.split(operator))
        
        # Validate that operands are digits and within length limits
        if not (a.isdigit() and b.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(a) > 4 or len(b) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Compute result
        total = str(int(a) + int(b)) if operator == '+' else str(int(a) - int(b))
        
        # Format each line and add to the appropriate list
        space = max(len(a), len(b)) + 2
        first_line.append(a.rjust(space))
        second_line.append(operator + ' ' + b.rjust(space - 2))
        dash_line.append('-' * space)
        total_line.append(total.rjust(space))
    
    # Join each line with appropriate spacing
    lines = [
    '    '.join(first_line), '    '.join(second_line),
    '    '.join(dash_line)]
    
    # Append results if requested
    if show_answers:
        lines.append('    '.join(total_line))
    
    # Returning the operations in the required format
    return '\n'.join(lines)