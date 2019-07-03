FROM python

RUN mkdir /app

WORKDIR /app

COPY ./app ./

RUN pip install -r ./requirements.txt

EXPOSE 5000

ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

CMD [ "flask", "run", "--host=0.0.0.0" ]