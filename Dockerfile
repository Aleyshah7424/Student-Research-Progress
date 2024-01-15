FROM python:3.9-slim

#Set the working directory
WORKDIR /research-image

#python scripts
COPY ./ /research-image//

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker image build -t research-app:1.0 ./
#docker tag research-app:1.0 ahmadalishah/research-app:1.0
