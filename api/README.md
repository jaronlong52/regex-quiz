# Activate venv
venv\Scripts\activate

# Run development:
python -m main 

# Build docker container:
docker build -t regex-api .

# Run docker container:
docker run -p 8080:8080 regex-api

# Tag image to artifact registry:
docker tag regex-api us-central1-docker.pkg.dev/regex-quiz-455418/regex-quiz/regex-api

# Push image to artifact registry:
docker push us-central1-docker.pkg.dev/regex-quiz-455418/regex-quiz/regex-api
