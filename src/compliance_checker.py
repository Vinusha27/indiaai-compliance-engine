import json

def check_compliance(extracted_data, rules):
    results = []
    
    # Ellaa page text-yum sethu single string ah maathuvom
    all_text = " ".join([page["content"].lower() for page in extracted_data if page["content"]])

    for rule in rules:
        found_keywords = [word for word in rule["keywords"] if word in all_text]
        is_compliant = len(found_keywords) > 0
        
        results.append({
            "rule_id": rule["rule_id"],
            "rule_name": rule["rule_name"],
            "status": "COMPLIANT" if is_compliant else "NON-COMPLIANT",
            "evidence_found": found_keywords,
            "description": rule["description"]
        })
    
    return results

if __name__ == "__main__":
    # Load extracted data
    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Load rules
    with open("src/rules.json", "r", encoding="utf-8") as f:
        rules = json.load(f)

    report = check_compliance(data, rules)

    print("\n--- AI COMPLIANCE REPORT ---")
    for r in report:
        print(f"[{r['status']}] {r['rule_name']}")
        if r['status'] == "COMPLIANT":
            print(f"   Evidence: Found keywords {r['evidence_found']}")
        else:
            print(f"   Action: Rule violation detected!")