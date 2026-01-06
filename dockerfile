FROM python:3.11-slim

# Set working directory inside container
WORKDIR / stud_record

# Copy application and test files
COPY student.py .
COPY test_student.py .

# Install pytest
RUN pip install --upgrade pip
RUN pip install pytest

# Run pytest inside Docker
RUN pytest --junitxml=pytest.xml

# Run the application with example arguments
CMD ["python", "student.py", "anannya", "bca", "3", "85", "90", "95"]
