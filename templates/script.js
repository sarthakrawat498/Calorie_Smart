document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission

    const data = {
        Gender: document.getElementById('Gender').value,
        Age: parseFloat(document.getElementById('Age').value),
        Height: parseFloat(document.getElementById('Height').value),
        Weight: parseFloat(document.getElementById('Weight').value),
        Duration: parseFloat(document.getElementById('Duration').value),
        Heart_Rate: parseFloat(document.getElementById('Heart_Rate').value),
        Body_Temp: parseFloat(document.getElementById('Body_Temp').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('result').innerText = `Calories Burned: ${result.Calories_Burned}`;
        } else {
            document.getElementById('result').innerText = `Error: ${result.error}`;
        }
    } catch (error) {
        document.getElementById('result').innerText = `Error: ${error.message}`;
    }
});
