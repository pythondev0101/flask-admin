from app import app

# TODO: Check mysql if running, turn on if not.
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
