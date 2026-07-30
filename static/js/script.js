let predictionData = {};

document.getElementById("predictionForm").addEventListener("submit", async function (e) {

    e.preventDefault();

    const fields = [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "view",
        "condition",
        "sqft_above",
        "sqft_basement",
        "yr_built",
        "yr_renovated"
    ];

    let data = {};

    for (let field of fields) {

        let value = document.getElementById(field).value.trim();

        if (value === "") {
            alert("Please fill all the fields.");
            return;
        }

        data[field] = Number(value);
    }

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    predictionData = {
        ...data,
        predicted_price: result["Predicted Price"]
    };

    const now = new Date();

    const date = now.toLocaleDateString();

    const time = now.toLocaleTimeString();

    document.getElementById("result").innerHTML = `

    <div class="result-card">

        <h2>🏠 Prediction Successful</h2>

        <h1>₹ ${Number(result["Predicted Price"]).toLocaleString()}</h1>

        <hr>

        <h3>Property Summary</h3>

        <p><strong>Bedrooms:</strong> ${data.bedrooms}</p>

        <p><strong>Bathrooms:</strong> ${data.bathrooms}</p>

        <p><strong>Living Area:</strong> ${data.sqft_living} sqft</p>

        <p><strong>Lot Area:</strong> ${data.sqft_lot} sqft</p>

        <p><strong>Floors:</strong> ${data.floors}</p>

        <hr>

        <p><strong>Date:</strong> ${date}</p>

        <p><strong>Time:</strong> ${time}</p>

    </div>

    `;

    document.getElementById("downloadBtn").style.display = "inline-block";

});


document.getElementById("downloadBtn").addEventListener("click", async function () {

    const response = await fetch("/download_report", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(predictionData)

    });

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "House_Price_Prediction_Report.pdf";

    document.body.appendChild(a);

    a.click();

    a.remove();

});