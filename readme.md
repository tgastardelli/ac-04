// criar container mysql
docker run -e MYSQL_ROOT_PASSWORD=Abcd321 --name mysql-A -d -p 3306:3306 --volume=/data/mysql-A:/var/lib/mysql mysql --bind-address=0.0.0.0

// shell do container
docker exec -it mysql-A bash

// conectar servidor MySQL
mysql -uroot -pAbcd321
