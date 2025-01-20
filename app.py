from flask import Flask, render_template, request
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

# Sample healthcare data for visualization
def generate_healthcare_data():
    # Example healthcare data: Revenue, Expenses for 6 months
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [100000, 120000, 110000, 130000, 125000, 140000],
        "Expenses": [80000, 95000, 90000, 105000, 102000, 110000]
    }
    df = pd.DataFrame(data)
    return df

# Financial calculations
def calculate_financials(revenue, expenses):
    profit = revenue - expenses
    return profit

# Create a Plotly graph for the dashboard
def create_dashboard_graph():
    df = generate_healthcare_data()
    
    # Revenue vs Expenses Bar Chart
    trace1 = go.Bar(
        x=df["Month"],
        y=df["Revenue"],
        name="Revenue",
        marker=dict(color='green')
    )
    trace2 = go.Bar(
        x=df["Month"],
        y=df["Expenses"],
        name="Expenses",
        marker=dict(color='red')
    )

    layout = go.Layout(
        title="Healthcare Revenue vs Expenses",
        barmode='group',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Amount ($)')
    )

    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return fig.to_html(full_html=False)

@app.route("/", methods=["GET", "POST"])
def home():
    profit = None
    dashboard_graph = create_dashboard_graph()
    
    if request.method == "POST":
        revenue = float(request.form.get("revenue"))
        expenses = float(request.form.get("expenses"))
        profit = calculate_financials(revenue, expenses)
    
    return render_template("index.html", profit=profit, dashboard_graph=dashboard_graph)

if __name__ == "__main__":
    app.run(debug=True)
