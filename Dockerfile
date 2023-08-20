FROM python:3.10.12

# Path: /site
WORKDIR /site

# Install dependencies
RUN apt update && apt install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
RUN git clone https://github.com/patpro28/ic3 .

# Install Python dependencies
RUN pip3 install -r requirements.txt