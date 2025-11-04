from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo pipeline
model = joblib.load("models/best_model.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            input_data = {
                "day_of_week": int(request.form["day_of_week"]),
                "is_weekend": int(request.form["is_weekend"]),
                "month": int(request.form["month"]),
                "store_area": float(request.form["store_area"]),
                "promotion": int(request.form["promotion"]),
                "holiday": int(request.form["holiday"]),
                "price_index": float(request.form["price_index"]),
                "competitor_distance_km": float(request.form["competitor_distance_km"]),
                "temperature_C": float(request.form["temperature_C"]),
                "foot_traffic": float(request.form["foot_traffic"]),
                "prev_day_sales": float(request.form["prev_day_sales"]),
            }

            df = pd.DataFrame([input_data])
            prediction = model.predict(df)[0]
            prediction = round(prediction, 2)

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)


@app.route("/variables")
def variables():
    return render_template("variables.html")


if __name__ == "__main__":
    app.run(debug=True)
