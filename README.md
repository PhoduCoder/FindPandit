# FindPandit
# An application that helps to find pandit for NRIs in USA
# This is a sample Flask Application. 

#To run the flask server locally 
export FLASK_APP=app.py
flask run

#Since we moved the app.py now inside the app folder
#now we should use the below commands

export FLASK_APP=app
export FLASK_ENV=development
flask run

#Had to additionally do this 
chmod a+x app.py