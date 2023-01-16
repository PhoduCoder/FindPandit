# FindPandit
Repository to create an application that helps to find pandit in USA

# To run the flask server locally 
export FLASK_APP=app.py
flask run

# Since we moved the app.py now inside the app folder
# now we should use the below commands
export FLASK_APP=app
export FLASK_ENV=development
flask run

# Had to additionally do this 
chmod a+x app.py