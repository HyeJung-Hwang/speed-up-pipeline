# Compare Parquet & CSV

### Git 레포지토리를 clone해주세요.
```bash
git clone https://github.com/HyeJung-Hwang/speed-up-pipeline.git
```

### Docker Image를 빌드해주세요.
```bash
docker build -t compare-pq-csv .
```

### Docker Container를 실행해주세요.
```bash
docker run -d -p 8888:8888 --name experiment-container compare-pq-csv
```

### 출력되는 url로 접속해주세요.
```bash
docker logs --tail 3 experiment-container
```