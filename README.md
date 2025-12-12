# 🔤 BASIC Interpreter

A custom programming language interpreter built from scratch in Python. Features a complete lexer, parser, and interpreter with both CLI and web interfaces.

## ✨ Features

- **Variable Assignment**: Store and retrieve values with `VAR` keyword
- **Arithmetic Operations**: `+`, `-`, `*`, `/`, `^` (power)
- **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical Operators**: `AND`, `OR`, `NOT`
- **Data Types**: Integers and floats
- **Built-in Constants**: `NULL`, `TRUE`, `FALSE`
- **Visual Error Messages**: Arrows point to exact error locations
- **Symbol Table**: Variable storage and retrieval
- **Multiple Interfaces**: Command-line, web UI, and AST visualizer

## 🎯 Language Syntax

### Variable Assignment
```
VAR x = 10
VAR y = 5.5
```

### Arithmetic Expressions
```
2 + 3 * 4
(10 - 5) / 2
2 ^ 3          # Power operation (equals 8)
```

### Comparisons
```
5 > 3          # Returns 1 (true)
10 == 10       # Returns 1 (true)
7 != 5         # Returns 1 (true)
```

### Logical Operations
```
1 AND 1        # Returns 1
1 OR 0         # Returns 1
NOT 0          # Returns 1
(5 > 3) AND (10 < 20)
```

### Complex Expressions
```
VAR result = (10 + 5) * 2 - 3
VAR comparison = (x > y) AND (y != 0)
```

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Ashita-Sharma/BASIC-Interpreter.git
cd BASIC-Interpreter

# Install Flask (for web interface)
pip install flask
```

### Command Line Interface

```bash
python main.py
```

**Interactive shell:**
```
basic > VAR x = 10
10
basic > VAR y = 5
5
basic > x + y
15
basic > x > y
1
```

### Web Interface

```bash
python application.py
```
Then open `http://localhost:5001` in your browser for a fully interactive web shell.

### AST Visualizer

```bash
python ast_demonstrator.py
```
Then open `http://localhost:5004` to see the Abstract Syntax Tree generation (without execution).

## 📋 Requirements

- Python 3.7+
- Flask (for web interface)

## 🏗️ Architecture

### 1. **Lexer** (Tokenization)
Converts source code into tokens:
```
"VAR x = 10" → [KEYWORD:VAR, IDENTIFIER:x, EQ, INT:10]
```

### 2. **Parser** (AST Generation)
Builds Abstract Syntax Tree from tokens following this grammar:

```
expr        : VAR IDENTIFIER = expr
            : comp-expr ((AND|OR) comp-expr)*

comp-expr   : NOT comp-expr
            : arith-expr ((==|!=|<|>|<=|>=) arith-expr)*

arith-expr  : term ((+|-) term)*

term        : factor ((*|/) factor)*

factor      : (+|-) factor
            : power

power       : atom (^ factor)*

atom        : INT|FLOAT|IDENTIFIER
            : ( expr )
```

### 3. **Interpreter** (Execution)
Traverses AST and executes operations using the Visitor pattern.

### 4. **Symbol Table**
Stores variables and their values with scope management.

## 🎨 Project Structure

```
BASIC-Interpreter/
├── basic.py                   # Full interpreter with execution
├── AST_basic.py              # AST-only version (no execution)
├── main.py                   # CLI interface
├── application.py            # Web interface (port 5001)
├── ast_demonstrator.py       # AST visualizer (port 5004)
├── string_with_arrows.py     # Error visualization utility
├── grammar.txt               # Language grammar specification
└── templates/
    ├── shell.html            # Web shell interface
    └── index.html            # AST visualizer interface
```

## 🔍 Error Handling

The interpreter provides detailed error messages with visual indicators:

```
basic > 5 + * 3
Invalid Syntax: Expected int or float
File <stdin>, line 1

5 + * 3
    ^
```

**Error Types:**
- `IllegalCharError`: Unknown character in source
- `InvalidSyntaxError`: Syntax rule violation
- `RTError`: Runtime errors (e.g., division by zero, undefined variables)

## 🔧 Customization

### Add New Operators
1. Add token type in `basic.py`:
```python
TT_MODULO = 'MODULO'
```

2. Update lexer in `make_tokens()`:
```python
elif self.current_char == '%':
    tokens.append(Token(TT_MODULO, pos_start=self.pos))
    self.advance()
```

3. Add interpreter method:
```python
def visit_ModuloNode(self, node, context):
    # Implementation
```

### Add New Keywords
Add to `KEYWORDS` list:
```python
KEYWORDS = ['VAR', 'AND', 'OR', 'NOT', 'IF', 'WHILE']  # etc.
```

## 📊 Built-in Constants

| Constant | Value | Usage |
|----------|-------|-------|
| `NULL` | 0 | Null/empty value |
| `TRUE` | 1 | Boolean true |
| `FALSE` | 0 | Boolean false |

## 🎯 Example Programs

**Calculate area of circle:**
```
VAR pi = 3.14159
VAR radius = 5
VAR area = pi * radius ^ 2
area
```

**Boolean logic:**
```
VAR age = 25
VAR hasLicense = 1
VAR canDrive = (age >= 18) AND hasLicense
canDrive
```

**Nested expressions:**
```
VAR x = 10
VAR y = 5
VAR result = ((x + y) * 2 - 10) / (x - y)
result
```

## 🐛 Troubleshooting

- **Module not found**: Install Flask with `pip install flask`
- **Port already in use**: Change port in `app.run(port=XXXX)`
- **Syntax errors**: Check grammar specification in `grammar.txt`

## 🎯 Future Enhancements

- [ ] Functions and procedures
- [ ] If/else conditional statements
- [ ] While/for loops
- [ ] String data type and operations
- [ ] Lists/arrays
- [ ] File I/O operations
- [ ] Import/module system
- [ ] Debugging mode with breakpoints
- [ ] Standard library functions (print, input, etc.)

## 📚 Learning Resources

- [Building a Programming Language](https://craftinginterpreters.com/)
- [Parser Theory](https://en.wikipedia.org/wiki/Parsing)
- [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:
- New language features
- Bug fixes
- Documentation improvements
- Performance optimizations

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👏 Acknowledgments

- Inspired by various interpreter tutorials and compiler design courses
- Built using Python's powerful class and visitor pattern features

## 📧 Contact

**Ashita Sharma**
- GitHub: [@Ashita-Sharma](https://github.com/Ashita-Sharma)

---

⭐ **Star this repo if you find it helpful!** ⭐

**Happy Interpreting! 💻🔤**
