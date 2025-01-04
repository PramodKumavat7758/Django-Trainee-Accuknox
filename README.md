# Django Trainee  - Accuknox
This project demonstrates the behavior of Django signals, particularly:

Whether signals run in the same thread as the caller.

Whether signals execute in the same database transaction as the caller.

The project uses the built-in SQLite database.

  

## Project Setup

### Ensure you have the following installed:

Python 3.x

Django 4.x or later

1. **Create Django Project**

You can install Django and start new project as follows:


```bash
pip install django
django-admin startproject signals_Demo
cd signals_Demo
python manage.py startapp users
```



2. **Add App to Installed Apps**
   1. Update INSTALLED_APPS in signal_demo/settings.py
      
      ```bash
      INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'users',  # Add this line
      ]
      ```
 

   

2. **Kubernetes Deployment :**
 
   1. Create Kubernetes deployment manifest files for deploying the Wisecow application in a Kubernetes environment. ex : deployment_manifests_kubernetes.yaml
   2. Create service file exposed as a Kubernetes service for accessibility. ex : service_manifests_kubernetes.yaml
   3. Apply the deployment and service using following commands.

   ```bash
   kubectl apply -f deployment_manifests_kubernetes.yaml
   kubectl apply -f service_manifests_kubernetes.yaml
   ```
      
   4. Check deployments and services running.Use commands.
      
    ```bash
   kubectl get deployments
   kubectl get services
   ```
    ![Kubernete  Service Deployment](status.png)
   
5. **Continuous Integration And Deployment**
   1.Github workflow for
   a. Create yaml file in ./github/workflows
   b. Set the secrets **secrets.DOCKER_USERNAME** and **secrets.DOCKER_PASSWORD** with your Dockerhub username and docker image name.
   
   ![workflow](workflow.png)

6. **TLS Implementaion**
   1. Install OpenSSL.
      
   ```bash
   sudo apt-get install openssl  
   ```
   ![openssl](openssl.png)

   
   2. Generate Private Key.
      
   ```bash
   openssl genrsa -out server.key 2048
   ```
   3. Generate Certificate Signing Request (CSR)
      
   ```bash
   openssl req -new -key server.key -out server.csr
   ```
   4. Self-Sign Certificate
      
   ```bash
   openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
   ```
![Certificate](sert.png)
   
   5. Deploy to Kubernetes. Reference this TLS secret in Kubernetes deployment configuration to enable TLS
      
   ```bash
   kubectl create secret tls tls-secret --cert=server.crt --key=server.key
   ```
7. **Output**
   ![WisecowRun](wisecowOutput.png)
---

Feel free to customize this README to provide more specific information about your project. Include any additional setup instructions, prerequisites, or specific details about your application that you think would be helpful for users.
