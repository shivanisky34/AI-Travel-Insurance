from flask import Flask, request, jsonify
import config

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query = req.get('queryResult', {}).get('queryText', '').lower()
    
    response_text = f"Welcome to {config.INSURANCE_PROVIDER} Assistant! How can I assist with your claim today?"
    
    if 'baggage' in query or 'lost' in query or 'luggage' in query:
        response_text = "For lost or delayed baggage claims, please share your flight number and PNR to initiate compensation processing."
    elif 'delay' in query or 'cancelled' in query or 'flight status' in query:
        response_text = "If your flight was delayed over 3 hours or cancelled, you may be eligible for full compensation or free re-booking."
    elif 'insurance' in query or 'policy' in query or 'claim' in query:
        response_text = "I can guide you through the claims process. Please provide your Policy Number to proceed."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(port=5000, debug=config.DEBUG_MODE)
