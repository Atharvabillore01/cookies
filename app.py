from flask import Flask, request, make_response

app = Flask(__name__)

# Homepage with the link
@app.route('/')
def home():
    response = make_response('<a href="/capture">Click me</a>')
    # Setting a test cookie
    response.set_cookie('test_cookie', 'cookie_value')
    return response

# Endpoint to capture cookies
@app.route('/capture')
def capture():
    cookies = request.cookies
    cookie_str = '<br>'.join([f'{key}: {value}' for key, value in cookies.items()])
    return f"Cookies captured:<br>{cookie_str}"

if __name__ == '__main__':
    app.run(debug=True)