FROM alpine:latest

WORKDIR /app

# Install Python and pip
RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    rm -rf /var/cache/apk/*

COPY . /app

# Create and activate a virtual environment
RUN python3 -m venv venv
RUN apk add --no-cache bash
RUN source venv/bin/activate && pip install --upgrade pip

# Install Python dependencies inside the virtual environment
#RUN source venv/bin/activate && pip install --no-cache-dir -r requirements.dev.txt
#RUN source venv/bin/activate && pip install pytest flake8 coverage apache-log-parser
RUN apk add py3-flask
CMD ["make", "run"]
