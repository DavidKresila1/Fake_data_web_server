import requests
from flask import Flask

app = Flask(__name__)

@app.route('/users/<int:userid>')
def get_user(userid):
    ip_address = '127.0.0.1:5000'  # Replace with the specific IP address
    url = f'http://{ip_address}/api/users/{userid}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        userID = data['userid']
        name = data['name']
        age = data['age']
        email = data['email']
        
        print(f"User ID: {userID}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"email: {email}")
            
        
        return f"User ID: {userID}, Name: {name}, Age: {age}, Email: {email}"
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Error"
    except (ValueError, KeyError) as e:
        print(f"Invalid JSON data: {e}")
        return "Invalid JSON data"

if __name__ == '__main__':
    app.run(port=8000)
