name := "meetup_dot_com_rsvp_stream_processing"

version := "1.0"

scalaVersion := "2.13.4"

libraryDependencies += "org.apache.spark" %% "spark-sql" % "3.1.0"

// https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10_2.12
libraryDependencies += "org.apache.spark" %% "spark-sql-kafka-0-10" % "3.1.0"

// https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients
libraryDependencies += "org.apache.kafka" % "kafka-clients" % "2.7.0"

// https://mvnrepository.com/artifact/mysql/mysql-connector-java
libraryDependencies += "mysql" % "mysql-connector-java" % "8.0.23"

// https://mvnrepository.com/artifact/org.mongodb.spark/mongo-spark-connector
libraryDependencies += "org.mongodb.spark" %% "mongo-spark-connector" % "10.2.2"

