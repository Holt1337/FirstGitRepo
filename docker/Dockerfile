FROM ubuntu

RUN apt-get update
RUN apt-get install -y git python3 python3-pip
ADD main.py /main.py
RUN pip install fastapi uvicorn[standart]
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]
