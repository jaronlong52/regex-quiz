# Activate venv
venv\Scripts\activate

# Run development:
python -m main 

# Build docker container:
docker build -t regex-api .

# Run docker container:
docker run -p 5000:5000 regex-api
