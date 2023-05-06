FROM python:3.11.2

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

# CMD ["uvicorn", "src.main:app", "--proxy-headers", "--port", "8000", "--reload"]
# CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]