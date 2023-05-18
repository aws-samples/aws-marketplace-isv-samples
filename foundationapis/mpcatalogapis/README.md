**Flask Application for Marketplace Catalog APIs**
This is a Flask application that demontrates the basic structure and functionality of a web application for Marketplace Catalog APIs using the Flask Framework. This application codebase usage is intended for Demo/Workshop/Lab in Development environment only and NOT meant for Production use. 

**Prerequisites**
Before running the application, ensure you have the following prerequesities installed: 
* Python 3.x [Python Installation Guide](https://www.python.org/downloads/)
* Flask: Install using ```pip install flask```

**Getting Started**: 
1. Clone the Github repository for sample codes: 
```git clone https://github.com/aws-samples/aws-marketplace-isv-samples ```

2. Change into project directory:
``` cd mpcatalogapis ```

3. Set up a virtual environment (optional but recommended)
``` python -m venv venv ```
``` source venv/bin/activate ```

4. Install the required dependencies: 
``` pip install -r requirements.txt ```

5. Start Flask Development application server: 
``` ./run.sh ```

6. Open your web browser and visit http://localhost:5000/ to see the application in action. 

**Project Structure**
The project structure follows a typical Flask application structure: 
* **app.py**: The main application file that initializes the Flask app and contains the first route / entry 
* **templates/**: Directory containing the HTML templates used by the application. 
* **static/**: Directory containing the CSS and JavaScript file used by the application. 
* **controllers/**: Directory containing the routes for Catalog Operations from UI. 
* **services/**: Directory containing the Marketplace Catalog Service API reference. 
* **requirements.txt**: List of required Python packages for the project. 

**Contributions** 
Contributions are welcome. If you have any suggestions or want to report an issue, please open an issue or submit a pull request. 

**License**
This project is licensed under the MIT License 

Feel free to customize the README file to fit the specific details and requirements of your Application. 
