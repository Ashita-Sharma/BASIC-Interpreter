from flask import Flask, render_template, request, jsonify
import basic

app = Flask(__name__)

conversation_history = []

@app.route('/')
def home():
    return render_template('shell.html')  # Make sure this line is correct

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    code = data.get('code', '')

    if not code.strip():
        return jsonify({'error': 'No code provided'})

    result, error = basic.run('<stdin>', code)

    if error:
        response = {
            'success': False,
            'output': error.as_string()
        }
    else:
        response = {
            'success': True,
            'output': str(result)
        }

    conversation_history.append({
        'input': code,
        'output': response['output'],
        'success': response['success']
    })

    return jsonify(response)

@app.route('/clear', methods=['POST'])
def clear():
    conversation_history.clear()
    basic.global_symbol_table.symbols.clear()
    basic.global_symbol_table.set("null", basic.Number(0))
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Changed to port 5001