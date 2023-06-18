from crud_server import app1
import os

if __name__ == "__main__":
    app1.run(debug=False,host='0.0.0.0', port=os.getenv('PORT_CRUD'))