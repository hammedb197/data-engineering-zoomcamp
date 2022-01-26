FROM python:3.9

RUN pip install pandas
RUN pip install SQLAlchemy
RUN pip install psycopg2


WORKDIR app/
COPY pipeline.py pipeline.py
COPY yellow_tripdata_2021-01.csv yellow_tripdata_2021-01.csv
ENTRYPOINT [ "python",  "pipeline.py"]
