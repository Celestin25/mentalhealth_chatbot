# mobile_chatbot_bn


## Overview ML
This app leverages a Machine Learning (ML) models and NLP to be able to questions depending on the input of users . It is built using TensorFlow and scikit-learn, employing a Multi-Layer Perceptron (MLP) neural network which is optimized and evaluated to ensure high accuracy and performance.
## Overview on website 
This app is built using React on front-end side,Django for back-end

## Model Development and Evaluation

### Features
- **Model Creation**: The MLP model includes multiple dense layers and uses regularization to prevent overfitting.
- **Training**: Optimally trained on a dataset with carefully selected hyperparameters for the best performance.
- **Evaluation**: Comprehensive evaluation metrics including accuracy, precision, recall, and F1-score are provided along with confusion matrix and classification reports.

## Pipeline Creation

### Functions
- Python functions encapsulate all steps of the ML pipeline, ensuring code modularity and reusability.
- **Retraining Mechanism**: A robust and well-documented mechanism for retraining the model with new data is included.



### GitHub Repository Structure
1. **README.md**: Provides detailed instructions for setting up and running the project.
2. **Model Files**: Includes Jupyter notebooks (`mental_health_chatbot.ipynb`) and Python scripts (`models.py`, `predictions.py`), detailing the model's development and deployment.
3. **Deployment Files**: Contains all necessary configurations for deploying the model on a cloud platform.
4. **URL**: Link to the deployed app (https://heart-disease-prediction-hbn5aqn8pzylyneftv7uhl.streamlit.app/). But they are another version will be deployed on AWS soon the one using React and Django.

## Deployment

- **Cloud Platform**: The ML pipeline is deployed on a cloud platform, ensuring scalability and easy access. The deployment is consistent with the development in the notebook and pipeline files.


### Prerequisites
Ensure you have Python and the necessary packages (`tensorflow`, `numpy`, `pandas`, `scikit-learn`) installed.
Ensure you have (Node.js (v18.x or higher)
npm (v8.x or higher)

### link to demo of the app:https://drive.google.com/file/d/1mvGw7HpfLOWOX929-gwv4KCZliLO8X5o/view?usp=drive_link

## Screenshot for english version

![image](https://github.com/user-attachments/assets/35d7c0da-6af0-4bd0-b0d5-dc7e6fb5b0f2)

## screenshot for kinyarwanda version

![image](https://github.com/user-attachments/assets/243f6403-21f0-424f-9dba-ea67c6f0a56f)

### Setup for front-end
1. Clone the repository:https://github.com/Celestin25/e-health-fn.git
2. Install dependencies by running :npm install
3.run  app: npm run dev 
### Setup for back-end
1.Clone the repository :https://github.com/Celestin25/health_chatbot_bn.git
2.Cd mental_health_project 
3.Create virtual environment 
4.run app : python manage.py runserver
