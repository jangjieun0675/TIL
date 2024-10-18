# EC2에서 Confluent Kafka 서버 설정

##1. EC2 인스턴스 생성
   - 인스턴스 실행

##2. EC2 접속
   - git bash를 사용하여 로컬에서 EC2로 접속:
     ```sh
     ssh -i "key.pem" ubuntu@EC2-IP 주소
     ```
   - root 권한을 부여하여 root 계정으로 전환:
     ```sh
     sudo su -
     ```
   - root 디렉토리로 이동:
     ```sh
     cd /
     ```
   - 엔진, 데이터, 로그 파일 생성:
     ```sh
     mkdir engn data log
     ```
   - engn 디렉터리와 그 하위 디렉토리까지 모든 사용자 권한 부여:
     ```sh
     chmod -R 777 /engn
     ```

##3. EC2 인스턴스에 파일 업로드/다운로드, 안전하게 연결하기 위해 설정
   - FileZilla에서 EC2 인스턴스를 사용시 사용자 이름 지정:
     - Ubuntu 인스턴스: `ubuntu`
     - Amazon Linux 인스턴스: `ec2-user`
   - Kafka 서버를 설치하고 실행하기 위한 필수 구성요소 /engn 폴더에 배치:
     - Confluent, OpenJDK, config.tar 파일

##4. Confluent 및 Java 파일 압축풀기
   - engn 디렉토리로 이동 후 Java, Confluent Kafka, config.tar 파일 압축풀기:
     ```sh
     tar -zxvf openjdk-11.0.0.2_linux-x64.tar.gz
     tar -zxvf confluent-7.7.1.tar.gz
     ln -s confluent-7.7.1 confluent
     cd confluent
     mv ../config.tar .
     tar -xvf config.tar
     ```

##5. Configuration 파일 수정
   - properties 파일 수정:
     - Kafka 브로커, Kraft controller, Confluent Control Center들의 설정을 포함하는 파일 수정
   - 스크립트 파일 수정:
     - scripts 디렉터리로 이동 후 start-broker.sh, start-controller.sh, start-control-center.sh 수정
   - 수정한 properties와 scripts를 다시 FileZilla를 통해 업로드
   - Log4j 설정 변경:
     ```sh
     cd log4j
     rm controller-log4j.properties
     cp broker-log4j.properties controller-log4j.properties
     ```

##6. Kafka UUID 생성
    ```sh
     cd /engn/confluent/bin
     ./kafka-storage random-uuid
     export JAVA_HOME=/engn/jdk-11.0.0.2
     ```

##7. 스토리지 포맷
    ```sh
    ./kafka-storage format -t <UUID> -c /engn/confluent/properties/controller.properties
    ./kafka-storage format -t <UUID> -c /engn/confluent/properties/broker.properties
     ```

##8. Kafka 서비스 실행
    ```sh
    cd /engn/confluent/scripts
    ./start-controller.sh
    ./start-broker.sh
    ./start-control-center.sh
    ```

##9. Kafka Topic 생성 및 테스트
    ```sh
    cd /engn/confluent/bin
    ./kafka-topics --bootstrap-server <EC2_IP>:9092 --create --topic basic_topic --partitions 3
    ./kafka-console-producer --broker-list <EC2_IP>:9092 --topic basic_topic
    ```

##10. Control Center 접속
    http://EC2_IP:9021
