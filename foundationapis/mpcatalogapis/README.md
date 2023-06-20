
**Overview of AWS Marketplace Catalog API**
The AWS Marketplace Catalog API service provides an API interface to manage AWS Marketplace for your AWS organization or AWS account. For approved sellers, you can manage your products programmatically, including the self-service publishing capabilities on the AWS Marketplace Management Portal.

With Catalog API actions, you can view and update your existing product programmatically. 
The AWS Marketplace Catalog API service provides standard AWS API functionality. You can directly use the REST API actions described in Actions, or you can use an AWS SDK to access an API that's tailored to the programming language or platform that you're using. For more information about using AWS SDKs, see [AWS SDKs](https://aws.amazon.com/developer/tools/#SDKs).

**Web-based reference application** 
This Github repository contains a sample web-based reference application for AWS Marketplace Catalog APIs to manage existing products present in the AWS Marketplace. The web-based reference application is built using [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.3.x/) - a micro web framework, to retrieve and update the products from AWS Marketplace Catalog.    

**API Integrations** 
AWS Marketplace integrates with the Catalog API actions to manage the products, offers and change requests. With Catalog API actions, you can view and update your existing products programmatically. The Catalog API actions used in this reference web application are: 

**ListEntities**: AWS Marketplace Catalog API action to retrieve the list of entities of a given type. 

**DescribeEntity**: AWS Marketplace Catalog API action to retrieve details of a given entity. 

**ListChangeSet**: AWS Marketplace Catalog API action to retrieve list of existing change requests. 

**DescribeChangeSet**:AWS Marketplace Catalog API action to retrieve details of a given change request id. 

**CanceChangeSet**: AWS Marketplace Catalog API action to cancel a given change request id. 

**ListTagsforResource**: AWS Marketplace Catalog API action to retrieve list of existing Tags for a given catalog resource. 

**TagResource**: AWS Marketplace Catalog API action to add a Tag for an existing catalog resource. 

**UntagResource**: AWS Marketplace Catalog API action to remove a Tag from an existing catalog resource. 


**Solution Overview**
To demonstrate the integration with AWS Marketplace Catalog APIs, the solution has a sample [Flask app](https://github.com/pallets/flask) which integrates with AWS Marketplace Catalog APIs. The flask-based web application has controllers to route incoming request to Catalog service. The Catalog service makes AWS Marketplace Catalog API actions to view and mange the products. The web pages are rendered using the html templates present in the reference web application. 

**Project Structure**
The project structure follows a typical Flask application structure: 
* **app.py**: The main application file that initializes the Flask app and contains the first route / entry 
* **templates/**: directory containing the HTML templates used by the application. 
* **static/**: directory containing the CSS and JavaScript file used by the application. 
* **controllers/**: directory containing the routes for Catalog Operations from UI. 
* **services/**: directory containing the Marketplace Catalog Service API reference. 
* **requirements.txt**: List of required Python packages for the project. 


**Prerequisites**
Before running the application, ensure you have the following prerequesities met and installed: 
* You must have an AWS account registered as a seller in AWS Marketplace.
* You must have one or more products listed in AWS Marketplace. 
* Python 3.x [Python Installation Guide](https://www.python.org/downloads/)
* Flask: Install using 
```shell
pip install flask
```

**Getting Started**: 
1. Clone the Github repository for sample codes: 
```shell
git clone https://github.com/aws-samples/aws-marketplace-isv-samples 
```

2. Change into project directory:
```shell 
cd foundationapis/mpcatalogapis 
```

3. Set up a virtual environment (optional but recommended)
```shell
python -m venv venv 
```
```shell 
source venv/bin/activate 
```

4. Install the required dependencies: 
```shell
pip install -r requirements.txt 
```

5. Start Flask Development application server: 
```shell 
chmod +x run.sh
./run.sh 
```

6. Open your web browser and visit http://localhost:5000/ to see the application in action. 


**Contributions** 
Contributions are welcome. If you have any suggestions or want to report an issue, please open an issue or submit a pull request. 

**License**
This project is licensed under the MIT-0 License 

Feel free to customize the README file to fit the specific details and requirements of your Application. 
