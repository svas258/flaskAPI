FROM postgres
COPY test.csv /tmp
COPY *.sql /docker-entrypoint-initdb.d/
ADD initial.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*

