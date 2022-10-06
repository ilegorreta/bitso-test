# Created by Ivan Legorreta
# Date: 05/10/2022
# Bitso Sr. Data Engineer Code Assessment

# Using python:slim as default base. This provides a good balance between size and functionality (i.e. alpine build is too slim).
# Also not setting a version - the implication of this is that the Python version auto-updates.

FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /workspaces

# Get requirements
COPY requirements.txt /workspaces

# Install needed packages (requirements.txt), directories and create credentials mount point.
RUN pip install -r /workspaces/requirements.txt

# Copy the code files and shell script to run them
COPY run.sh /workspaces
COPY src /workspaces/src
COPY data /workspaces/data

# Run the shell script when the container launches
CMD ["/bin/bash" , "run.sh"]