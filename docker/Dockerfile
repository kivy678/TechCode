FROM 	[HOST]:[PORT]/mariadb:1.0
LABEL	"maintainer"="Create Base Image"

ENV 	MYSQL_ROOT_PASSWORD=hellow world
ENV 	TZ=Asia/Seoul

EXPOSE 3606

RUN	["apt-get", "update"]
RUN	["apt-get", "install", "-y", "vim"]

# cp my.cnf
ADD	my.cnf 	/etc/mysql/my.cnf
RUN 	["chmod", "644", "/etc/mysql/my.cnf"]

#init database
ADD 	schema	/docker-entrypoint-initdb.d
