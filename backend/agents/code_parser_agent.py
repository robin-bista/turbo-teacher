import ast
import json
import openai

class CodeParserAgent:
    def __init__(self, sambanova_endpoint, api_key):
        self.sambanova_endpoint = sambanova_endpoint
        self.api_key = api_key
        self.language = "Unknown"  # Default until detected
        self.client = openai.OpenAI(
                    api_key=self.api_key,
                    base_url=self.sambanova_endpoint)

    def parse_code(self, code):
        """Parses code using Python's AST and SambaNova for advanced analysis."""
        try:
            # Step 1: Use AST for basic syntax parsing
            tree = ast.parse(code)
            tokens = [node for node in ast.walk(tree)]
            structure = [type(token).__name__ for token in tokens]
        except SyntaxError as e:
            return {"error": f"Syntax Error: {e}"}

        # Step 2: Use SambaNova for advanced parsing
        advanced_analysis = self.analyze_with_sambanova(code)

        # Combine results from AST and SambaNova
        return {
            "language": advanced_analysis.get("language", "Unknown"),
            "structure": advanced_analysis.get("structure", structure),  # Use AST structure as fallback
            "status": advanced_analysis.get("status", "Parsing failed"),
            "explanation": advanced_analysis.get("explanation", "No explanation provided.")
        }

    def analyze_with_sambanova(self, code):
        """Send the code snippet to SambaNova's API for detailed analysis."""
        try:
            response = self.client.chat.completions.create(
                model='Meta-Llama-3.1-405B-Instruct',
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                            You are an expert code parser. Parse the following code and return only a JSON object with the following fields:
                            - "language": Detected programming language.
                            - "structure": A structured breakdown of the code (functions, variables, statements).
                            - "status": Parsing status (e.g., "Parsed successfully").
                            - "explanation": A brief explanation of what the code does.
                            Code: {code}
                        """
                    }
                ],
                temperature=0.0,
                top_p=0.0,
            )

            raw_response = response.choices[0].message.content.strip()
            print("SambaNova Raw Response:", raw_response)  # Debug log

            # Extract JSON portion from the response
            json_start = raw_response.find("{")
            json_end = raw_response.rfind("}") + 1
            json_text = raw_response[json_start:json_end]

            return json.loads(json_text)  # Parse and return JSON
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", str(e))  # Debug log
            return {"error": "Invalid JSON format from SambaNova"}
        except Exception as e:
            print("SambaNova API Error:", str(e))  # Debug log
            return {"error": f"SambaNova API Error: {str(e)}"}

