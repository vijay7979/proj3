FROM python:3
WORKDIR \Users\v_vj\Documents\cs50\p3\proj3
ADD requirements.txt \Users\v_vj\Documents\cs50\p3\proj3
RUN pip install -r requirements.txt
ADD . \Users\v_vj\Documents\cs50\p3\proj3