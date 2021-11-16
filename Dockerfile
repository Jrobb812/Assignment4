FROM alpine:3.8
RUN apk add python3 py-pip && python3 -m ensurepip && pip install --upgrade pip && pip install flask
WORKDIR 
COPY . /app/
ENTRYPOINT ["python"]
CMD ["assignment4.py"]