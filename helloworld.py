'''
Created on 04-Sep-2019

@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
from model import Dbsession, User
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    user_detail = get_user_details()
    user_name = "Default user"
    if user_detail:
       user_name = f"{user_detail.first_name} {user_detail.last_name}"
    return f'Hello, {user_name}!'
    

def get_user_details():
    try:
        user_detail = (Dbsession.query(User.first_name, User.last_name).first())
        if not user_detail:
            return False
        return user_detail
    except Exception as err:
        print(f"Error while getting the user details reason {err}")
        return False
    finally:
        Dbsession.close()

if __name__ == '__main__':  # Script executed directly?
    print("Hello ! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
