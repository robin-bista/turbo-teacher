from flask import Flask, request, jsonify
from agents.code_parser_agent import CodeParserAgent  # Import the agent
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize CodeParserAgent with SambaNova credentials
SAMBANOVA_ENDPOINT = "https://api.sambanova.ai/v1"
SAMBANOVA_API_KEY = "61c2c66e-e93d-4345-aadc-05ca16f2c248" 

parser_agent = CodeParserAgent(SAMBANOVA_ENDPOINT, SAMBANOVA_API_KEY)

@app.route('/api/parse-code', methods=['POST'])
def parse_code():
    """Endpoint to receive code and return parsed results."""
    data = request.get_json()
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Use the CodeParserAgent to process the code
    result = parser_agent.parse_code(code)

    # Debug log to inspect the backend response
    print("Backend Response:", result)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)