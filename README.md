# Calorie Smart

Calorie Smart is a machine learning-based application that predicts the number of calories burned based on various inputs. The project uses multiple regression models to provide accurate predictions.

## Features
- **Machine Learning Models**: Implements Linear Regression, Decision Tree Regression, Random Forest Regression, and XGBoost Regressor.
- **Dataset**: Uses a dataset from Kaggle to train and validate the models.
- **Interactive UI**: Provides a user-friendly interface to input data and receive predictions.
- **Data Visualization**: Displays insights into calorie-burning trends.

## Project Structure
```
Calorie_Smart/
│── templates/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│── venv/ (Virtual Environment)
│── app.py (Main application script)
│── calorie_model.pkl (Trained ML model)
│── Calories_Burnt_Prediction.ipynb (Jupyter Notebook for model training)
│── calories.csv (Dataset file)
│── exercise.csv (Additional dataset file)
│── LICENSE
│── requirements.txt (Dependencies list)
```

## Installation & Usage

### 1. Clone the Repository
```sh
git clone https://github.com/sarthakrawat498/Calorie_Smart.git
cd Calorie_Smart
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```

The application should now be running locally. Open `http://127.0.0.1:5000/` in your browser to access it.

## Technologies Used
- Python
- Flask
- Machine Learning (Scikit-Learn, XGBoost)
- HTML, CSS, JavaScript

## Contributing
Feel free to fork this repository, submit issues, or open pull requests to enhance the project!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Made with ❤️ by [sarthakrawat498](https://github.com/sarthakrawat498)

