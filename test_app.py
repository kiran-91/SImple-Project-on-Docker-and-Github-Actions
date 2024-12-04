from app import app

# we need to start the function name with test 
def test_home():
    response=app.test_client().get("/")
    
    assert response.status_code==200
    assert response.data==b"Hello World!"
     