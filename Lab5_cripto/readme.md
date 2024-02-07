sudo docker build -t c1 -f c1.dockerfile .
sudo docker build -t c2 -f c2.dockerfile .
sudo docker build -t c3 -f c3.dockerfile .
sudo docker build -t c4s1 -f c4s1.dockerfile .
sudo docker build -t p3 -f p3.dockerfile .

sudo docker run -it c1 bash
sudo docker run -it c2 bash
sudo docker run -it c2 bash
sudo docker run --cap-add=NET_RAW --cap-add=NET_ADMIN -it c4s1 bash
sudo docker run --cap-add=NET_RAW --cap-add=NET_ADMIN -it p3 bash

sudo docker exec -it da6bc1588181 /bin/bash
sudo tshark -i lo -w /tmp/trafico.pcapng
docker cp da6bc1588181:/tmp/trafico.pcapng .


En c4s1 ifconfig.
service ssh status - estado del servidor
service ssh start - inicia el servidor

En cliente 1,2 y 3.
ssh test@172.17.0.5 - conectar al servidor con contraseña test
En cliente 4
ssh test@localhost




sudo apt-get update && sudo apt-get install -y autoconf libssl-dev zlib1g-dev gcc make git vim
git clone https://github.com/openssh/openssh-portable
cd openssh-portable
vim version.h
autoreconf
./configure
make && make tests