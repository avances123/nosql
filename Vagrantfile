# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "centos65"


  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.

  

  config.vm.define "mongo1" do |mongo1|
	mongo1.vm.hostname = "mongo1"
  	mongo1.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "256"]
    end

	mongo1.vm.network :private_network, ip: "192.168.111.11"
  	mongo1.vm.network :forwarded_port, guest: 8888, host: 8880

    mongo1.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "files/mongodb/hosts"
      ansible.playbook = "files/mongodb/site.yml"
    end
  end

  config.vm.define "mongo2" do |mongo2|
	mongo2.vm.hostname = "mongo2"
  	mongo2.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "256"]
    end
	mongo2.vm.network :private_network, ip: "192.168.111.12"
  	mongo2.vm.network :forwarded_port, guest: 8888, host: 8881

    mongo2.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "files/mongodb/hosts"
      ansible.playbook = "files/mongodb/site.yml"
    end
  end

  config.vm.define "mongo3" do |mongo3|
	mongo3.vm.hostname = "mongo3"
  	mongo3.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "256"]
    end
	mongo3.vm.network :private_network, ip: "192.168.111.13"
  	mongo3.vm.network :forwarded_port, guest: 8888, host: 8882

    mongo3.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "files/mongodb/hosts"
      ansible.playbook = "files/mongodb/site.yml"
    end
  end

  config.vm.define "mongo4" do |mongo4|
	mongo4.vm.hostname = "mongo4"
  	mongo4.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "256"]
    end
	mongo4.vm.network :private_network, ip: "192.168.111.14"
  	mongo4.vm.network :forwarded_port, guest: 8888, host: 8883

    mongo4.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "files/mongodb/hosts"
      ansible.playbook = "files/mongodb/site.yml"
    end
  end

 
end
