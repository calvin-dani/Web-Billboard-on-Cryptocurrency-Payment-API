from analytics_server import analytics_app
import os
if __name__ == "__main__":
    analytics_app.config['DEBUG'] = False
    analytics_app.config['MONGO_URI'] = os.getenv('DB_URI')
    analytics_app.run(debug=False,host='0.0.0.0', port=os.getenv('PORT_ANALYTICS'))