# Vote.com
It is a real-time election voting system. The system is built using Python, Kafka, Spark Streaming, Postgres and Streamlit. The system is built using Docker Compose to easily spin up the required services in Docker containers.

## System Architecture
![system_architecture.jpg](images%2Fsystem_architecture.jpg)

### Run
1. Clone this repository.
2. Navigate to the root containing the Docker Compose file.
3. Run the following command:

```bash
docker-compose up -d
```
This command will start Zookeeper, Kafka and Postgres containers in detached mode (`-d` flag). Kafka will be accessible at `localhost:9092` and Postgres at `localhost:5432`.

##### Additional Configuration
If you need to modify Zookeeper configurations or change the exposed port, you can update the `docker-compose.yml` file according to your requirements.

### Running the App
1. Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

2. Creating the required tables on Postgres and generating voter information on Kafka topic:

```bash
python main.py
```

3. Consuming the voter information from Kafka topic, generating voting data and producing data to Kafka topic:

```bash
python voting.py
```

4. Consuming the voting data from Kafka topic, enriching the data from Postgres and producing data to specific topics on Kafka:

```bash
python spark-streaming.py
```

5. Running the Streamlit app:

```bash
streamlit run streamlit-app.py
```

### Picture
![dashboard_image.png](images%2Fdashboard_image.png)
