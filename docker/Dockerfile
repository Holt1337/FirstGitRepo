FROM ubuntu


RUN apt-get update
RUN apt-get install -y git python3 python3-pip

ADD README.md /README.md
ADD print_hello /bin/print_hello

ADD main.py /main.py
RUN pip install fastapi uvicorn[standart]
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]
RUN useradd -ms /bin/bash deploy2022user
USER deploy2022user
#docker run --rm -it -p 8988:8000  --name python my-image
#docker build -t my-image .
#docker run --rm -it -v $PWD/data:/data ubuntu