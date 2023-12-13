FROM python:slim
WORKDIR /app
ADD . .
EXPOSE 8501
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "streamlit run ./webui.py & python -u ./main.py"]