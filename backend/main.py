from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    	print("test for cont")
	return {"Hello": "World"}
	
