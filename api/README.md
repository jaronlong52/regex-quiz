# Activate venv
venv\Scripts\activate

# Run development:
python -m main 

# Build docker container:
docker build -t python-imagename .

# Run docker container:
docker run python-imagename
