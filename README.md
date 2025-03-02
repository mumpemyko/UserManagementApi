#UserManagement API #
This flask app allows the client to GET users in memory and also add new user with the help of blueprints(user_bp)
#installation steps #
Clone this repository 
#endpoints #
 @app.route('/users', methods=[‘GET’])  – returns the users in memory
@app.route('/users', methods=[‘POST’]) – adds a new user to the list


#requirements#
Python 3.x
