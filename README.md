# Vote.com
It is a real-time voting system. The used technologies are Python, Kafka, Spark Streaming, Postgres SQL, Docker, and Streamlit.

## System Architecture
![system_architecture](https://github.com/roniskywalker/Vote.com/assets/97012708/a8ef3bca-9db1-4729-8d55-8214c033d945)

### Run
1. Clone this repository.
2. Run the command to set docker:
```bash
docker-compose up -d
```
3. Run the following command to start the app:
I. Install the required Python packages:
```bash
pip install -r requirements.txt
```
II. Create the tables on Postgres and generate voter information on the Kafka topic:
```bash
python main.py
```
III. Consume the voter information from the Kafka topic, generating voting data, and producing data for the Kafka topic:
```bash
python voting.py
```
IV. Consume the voting data from Kafka topic, enriching the data from Postgres and producing data to specific topics on Kafka:
```bash
python spark-streaming.py
```
V. Run the Streamlit app:
```bash
streamlit run streamlit-app.py
```

### Picture
![dashboard_image](https://github.com/roniskywalker/Vote.com/assets/97012708/2739ce81-7688-4162-bebe-14b68b6d76b5)
