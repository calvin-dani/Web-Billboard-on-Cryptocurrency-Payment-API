from crud_server import app1
import os

if __name__ == "__main__":
    app1.config['DEBUG'] = False
    app1.config['MONGO_URI'] = os.getenv('DB_URI')
    app1.run(debug=False,host='0.0.0.0', port=os.getenv('PORT_CRUD'))