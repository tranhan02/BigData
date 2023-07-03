FROM python:3.11
WORKDIR /app

COPY crawl_data.py .
COPY coin.csv .
COPY get_list_coin.py .

RUN pip install cryptocmd

RUN pip install pandas

RUN pip install requests

CMD ["python", "./crawl_data.py"]