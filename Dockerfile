# Created by Ivan Legorreta
# Date: 05/10/2022
# Bitso Sr. Data Engineer Code Assessment

# Using python:slim as default base. This provides a good balance between size and functionality (i.e. alpine build is too slim).
# Also not setting a version - the implication of this is that the Python version auto-updates.

FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Get requirements
COPY requirements.txt /app

# Install needed packages (requirements.txt), directories and create credentials mount point.
RUN pip install -r /app/requirements.txt

# Switch to a non-root users to increase security
RUN groupadd -r appuser && \
    useradd -r -g appuser -d /app appuser && \
    chown -R appuser /app 
USER appuser

# Copy the code files and shell script to run them
# COPY run.sh /app
COPY src /app/src

# Run the shell script when the container launches
# CMD ["/bin/bash" , "run.sh"]