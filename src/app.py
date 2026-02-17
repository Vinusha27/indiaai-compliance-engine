from flask import Flask, render_template, request
import os
import pdfplumber
import json

app = Flask(__name__, template_folder='../templates')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def analyze_pdf(path):
    text_data = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text_data += (page.extract_text() or "") + " "
    
    # rules.json un src folder-la irukkanum
    rules_path = os.path.join(os.path.dirname(__file__), 'rules.json')
    if not os.path.exists(rules_path):
        return [{"rule_id": "Error", "rule_name": "rules.json not found", "status": "ERROR", "evidence_found": []}]

    with open(rules_path, 'r') as f:
        rules = json.load(f)

    results = []
    text_lower = text_data.lower()
    for rule in rules:
        found = [w for w in rule["keywords"] if w in text_lower]
        results.append({
            "rule_id": rule["rule_id"],
            "rule_name": rule["rule_name"],
            "status": "COMPLIANT" if found else "NON-COMPLIANT",
            "evidence_found": found
        })
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            results = analyze_pdf(path)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)