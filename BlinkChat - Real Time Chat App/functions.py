import pyrebase
import requests
from groq import Groq
from datetime import datetime
import pandas as pd

# Firebase Configuration
firebase_config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def sign_up(email, password, name):
    """Sign up a new user, send email verification, and store user details"""
    try:
        user = auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['idToken'])
        
        user_id = user['localId']
        id_token = user['idToken']  # Get the authentication token

        db.child("users").child(user_id).set(
            {"name": name, "email": email},
            token=id_token  # Pass the token for authentication
        )
        return user
    except Exception as e:
        return None


def send_verification_email(user_email, user_password):
    try:
        user = auth.sign_in_with_email_and_password(user_email, user_password)
        auth.send_email_verification(user['idToken'])
        return True
    except Exception as e:
        return False


def sign_in(email, password):
    """Sign in user only if email is verified"""
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception:
        return None
    
def user_is_verifiaction(token):
    user_info = auth.get_account_info(token)
    if not user_info['users'][0]['emailVerified']:
        return False
    else:
        return True

def reset_password(email):
    """Send a password reset email"""
    try:
        auth.send_password_reset_email(email)
        return True
    except Exception:
        return False

def change_password(user, new_password):
    """Change the user's password (User must be signed in)"""
    try:
        auth.update_user(user['idToken'], password=new_password)
        return True
    except Exception:
        return None
    
def get_user_data(user_id, id_token):
    """Retrieve user data from Firebase Database"""
    try:
        user_data = db.child("users").child(user_id).get(token=id_token)
        if user_data.val():
            return user_data.val()
        else:
            return {"error": "No user data found for the given ID."}
    except Exception as e:
        return {"error": str(e)}


def add_friend_in_chat(name, user_email, add_email, user_idtoken):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    chat_id = f"{fixed_mail}"

    message_data = {
        "name": name,
        "email": add_email,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/users_friends/{chat_id}.json?auth={user_idtoken}"
    response = requests.post(url, json=message_data)

    if response.status_code == 200:
        return True
    else:
        return False
    

        
def get_friends_in_chat(user_email, user_idtoken):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    chat_id = f"{fixed_mail}"
    
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/users_friends/{chat_id}.json?auth={user_idtoken}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
def get_all_users(user_idtoken):
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/users/.json?auth={user_idtoken}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
def send_user_message(user_email, friend_email, message, user_idtoken):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    fixed_mail_2 = friend_email.replace("@", "_").replace(".", "_")
    chat_id = f"{fixed_mail}_{fixed_mail_2}"
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/messages/{chat_id}.json?auth={user_idtoken}"
    response = requests.post(url, json=message)
    if response.status_code == 200:
        return response.json()
    
def load_user_message(user_email, friend_email, user_idtoken):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    fixed_mail_2 = friend_email.replace("@", "_").replace(".", "_")
    chat_id = f"{fixed_mail}_{fixed_mail_2}"
    
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/messages/{chat_id}.json?auth={user_idtoken}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
def delete_friend_chats_yes_do(user_email, friend_email, user_idtoken):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    fixed_mail_2 = friend_email.replace("@", "_").replace(".", "_")
    chat_id = f"{fixed_mail}_{fixed_mail_2}"
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/messages/{chat_id}.json?auth={user_idtoken}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    else:
        return False


def block_user_friend(user_email, friend_email, friend_name, user_idtoken):
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/block_users_friends/{user_email.replace(".", "-")}.json?auth={user_idtoken}"
    response = requests.post(url, json={"name" : friend_name, "email" : friend_email})
    if response.status_code == 200:
        return True
    else:
        return False
    
def get_block_friend(user_email, user_idtoken):
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/block_users_friends/{user_email.replace(".", "-")}.json?auth={user_idtoken}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json() 


def unblock_user_friend(user_email, friend_id, user_idtoken):
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/block_users_friends/{user_email.replace(".", "-")}/{friend_id}.json?auth={user_idtoken}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    else:
        return False

def get_ai_answer(Conversation):
    data = pd.read_csv("chatbot_config.csv")
    api = data["api_key"][0]
    temperature = int(data["temperature"][0])
    max_tokens = int(data["max_tokens"][0])
    top_p = int(data["top_p"][0])
    stream = bool(data["stream"][0])  # ✅ Convert directly to bool
    model = data["model"][0]
    client = Groq(api_key=api)
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=Conversation,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=stream  # ✅ Now correctly formatted as a boolean
        )
        answer = completion.choices[0].message.content.strip()
        return answer  

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, there was an error processing your request."



def get_chatbot_config_data(token):
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/chatbot_Configuration.json?auth={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def add_new_chat(user_email, friend_email, friend_name, time, token):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_new_messages/{fixed_mail}.json?auth={token}"
    response = requests.post(url, json={"name": friend_name, "email": friend_email, "time":time})
    if response.status_code == 200:
        return True
    else:
        return False
    
def get_new_chats(user_email, token):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_new_messages/{fixed_mail}.json?auth={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def remove_new_chat(user_email, id, token):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_new_messages/{fixed_mail}/{id}.json?auth={token}"
    response = requests.delete(url)
    if response.status_code == 200:
        return True
    else:
        return False
    
def add_status(user_email, user_name, user_status, time, token):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")  # Convert email to a valid key
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_status/{fixed_mail}.json?auth={token}"
    
    data = {
        "name": user_name,
        "email": user_email,
        "status": user_status,
        "time": time
    }

    response = requests.put(url, json=data)  # Use PUT to store under the email key

    return response.status_code == 200 
    
import requests

def get_all_status(user_friends_email_list, token):
    statuses = {}  # Dictionary to store all friends' statuses

    for email in user_friends_email_list:
        fixed_mail = email.replace("@", "_").replace(".", "_")
        url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_status/{fixed_mail}.json?auth={token}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:  # Only add if data is not empty
                statuses[email] = data
        else:
            statuses[email] = None  # Indicate failure for this friend

    return statuses  # Return all statuses as a dictionary

def delete_user_status(user_email, token):
    fixed_mail = user_email.replace("@", "_").replace(".", "_")
    url = f"https://blinkchatofficial-default-rtdb.firebaseio.com/user_status/{fixed_mail}.json?auth={token}"
    
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    else:
        return False
