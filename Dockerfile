# 
FROM python:3.9.9

# 
WORKDIR /code

# sudo apt-get update.
# sudo apt-get upgrade.
# sudo apt install poppler-utils.

RUN pip install --no-cache-dir --upgrade python-dotenv==0.21.1
RUN pip install --no-cache-dir --upgrade fastapi
RUN pip install --no-cache-dir --upgrade faiss-cpu
RUN pip install --no-cache-dir --upgrade uvicorn
RUN pip install --no-cache-dir --upgrade requests
RUN pip install --no-cache-dir --upgrade notion
RUN pip install --no-cache-dir --upgrade schedule



COPY ./app /code/app

ENV PYTHONPATH "${PYTHONPATH}:/code/app"


WORKDIR /code/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]