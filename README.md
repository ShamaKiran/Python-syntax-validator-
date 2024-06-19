# Python-syntax-validator-
The main purpose of this project is to create a tool that can validate and parse a subset of Python expressions involving the zip function,arithmetic operator,function definition,sets and tuples. This helps in understanding concepts like lexical analysis and parsing, or as a component in a larger project where validating specific kinds of Python expressions is necessary.

How It Works
The user is prompted to enter a zip function expression.
The lexer breaks down this expression into tokens.
The parser checks if the sequence of tokens conforms to the grammar rules defined for a valid zip function.
If the expression is valid, a success message is displayed; otherwise, an error message indicates the nature of the syntax error.
This project illustrates the basic principles of creating a custom lexer and parser using the ply library in Python.






