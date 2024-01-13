FROM python:3.9-slim

#Set the working directory
WORKDIR /app

#python scripts
COPY main.py .
COPY university.py .
COPY student.py .
COPY researchproject.py .

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker build -t ResearchProgress-app
# docker run ResearchProgress-app 
