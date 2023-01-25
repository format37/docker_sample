# Docker server sample
This sample can be used as scratch for a new project  
  
### Docker installation:
```
wget -qO- https://get.docker.com/ | sh
sudo apt install python3-pip
sudo pip install docker-compose
```
### Portainer installation (optional):
```
sudo docker volume create portainer_data
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce:2.9.3
```
### Project installation:
* Clone the repository
```
# if not exists
mkdir ~/projects -p && cd ~/projects
https://github.com/format37/docker_sample.git
cd docker_sample
```
* Compose:
```
sh compose.sh
```
### Test:
```
cd client
python3 request.py
```
