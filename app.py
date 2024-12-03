from flask import Flask, request, render_template

app = Flask(__name__)

# Financial data for companies
financial_data = {
    "Microsoft": {
        "Total Revenue": "$198B",
        "Net Income Change": "10% increase",
        "Total Assets": "$410B"
    },
    "Tesla": {
        "Total Revenue": "$82B",
        "Net Income Change": "15% increase",
        "Total Assets": "$99B"
    },
    "Apple": {
        "Total Revenue": "$394B",
        "Net Income Change": "8% increase",
        "Total Assets": "$352B"
    }
}

# Function to handle predefined queries
def chatbot_response(query):
    if query == "What is the total revenue?":
        return "\n".join(
            [f"{company}: {data['Total Revenue']}" for company, data in financial_data.items()]
        )
    elif query == "How has net income changed over the last year?":
        return "\n".join(
            [f"{company}: {data['Net Income Change']}" for company, data in financial_data.items()]
        )
    elif query == "What are the total assets for this fiscal year?":
        return "\n".join(
            [f"{company}: {data['Total Assets']}" for company, data in financial_data.items()]
        )
    else:
        return "Sorry, I can only respond to predefined queries."

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot response route
@app.route("/get_response", methods=["POST"])
def get_response():
    user_query = request.form["query"]
    response = chatbot_response(user_query)
    return render_template("index.html", query=user_query, response=response)

if __name__ == "__main__":
    app.run(debug=True)
