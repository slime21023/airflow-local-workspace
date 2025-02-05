FROM bitnami/airflow:2.7.0
WORKDIR /opt/airflow
ENV AIRFLOW_HOME=/opt/airflow

USER root

CMD ["airflow", "standalone"]