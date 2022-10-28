FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirementx.txt /code/
RUN pip install -r requirementx.txt
COPY . /code/
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000