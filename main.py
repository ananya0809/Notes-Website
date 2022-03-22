from website import create_app

app = create_app()

#start a webserver
#everytime there is a change to the python code, it will
#automatically re-run the webserver. -> (debug = True)
if __name__ == '__main__': #only run not import this file
    app.run(debug=True) #runs webserver only if main.py is run