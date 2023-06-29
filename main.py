from website import create_app
# from db import *


# connectoToDB()
app  = create_app()
if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     return "Website content goes here."

# if __name__ =='__main__':
#     app.run(debug=True)