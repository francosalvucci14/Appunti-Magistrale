
Documentazione GNS3 https://docs.gns3.com/docs/getting-started/installation/linux/

![](attachments/Pasted%20image%2020250514093412.png)

# Installazone Ubuntu

```bash
sudo add-apt-repository ppa:gns3/ppa
sudo apt update                                
sudo apt install gns3-gui gns3-server
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable"

sudo apt update
sudo apt install docker-ce

sudo usermod -aG ubridge libvirt kvm wireshark docker gnubbo
```


# Installazione Debian

Su Debian è **necessario** aggiungere i plugins **ubridge** e **dynamips**

```bash
sudo apt install git build-essential pcaputils  libpcap-dev

git clone https://github.com/GNS3/ubridge.git

cd ubridge
make
sudo make install



sudo apt install libelf-dev libpcap-dev cmake

git clone https://github.com/GNS3/dynamips.git

cd dynamips

mkdir build
cd build
cmake ..
sudo make install


for i in ubridge docker wireshark; do
 sudo usermod -aG $i $USER
done
```