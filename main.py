from website import create_app
# from db import *



app  = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True) #Ajuste para correr enn replit, que ocupa ue sea host 0.0.0.0
    # app.run(debug=True)

# @app.route('/')
# def home():
#     return "Website content goes here."

# if __name__ =='__main__':
#     app.run(debug=True)