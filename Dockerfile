FROM apache/airflow:2.8.2
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install apache-airflow==2.8.2
