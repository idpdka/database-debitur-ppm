from app import app

app.run(ssl_context=('certificates/cert.pem', 'certificates/key.pem'), host = '0.0.0.0', port = '3124', threaded=True, debug=True)
