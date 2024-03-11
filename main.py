from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"Personal Details": {'name': 'Kamran'}}

@app.get('/About')
def about():
    return {'data': 'About Page'}