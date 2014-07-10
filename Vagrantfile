Vagrant.configure('2') do |config|
  config.vm.define 'precise64' do |precise64|
    precise64.vm.box = 'hashicorp/precise64'
    precise64.vm.network 'private_network', ip: '192.168.0.51'
    precise64.vm.network 'forwarded_port', guest: 8000, host: 8080
    precise64.vm.synced_folder '../../Packages/bambu-bootstrap/bambu_bootstrap', '/home/vagrant/lib/python2.7/site-packages/bambu_bootstrap'
    precise64.vm.synced_folder '../../Packages/bambu-cron/bambu_cron', '/home/vagrant/lib/python2.7/site-packages/bambu_cron'
    precise64.vm.synced_folder '../../Packages/bambu-mail/bambu_mail', '/home/vagrant/lib/python2.7/site-packages/bambu_mail'
    precise64.vm.synced_folder '../../Packages/bambu-markup/bambu_markup', '/home/vagrant/lib/python2.7/site-packages/bambu_markup'

    precise64.vm.provision 'ansible' do |ansible|
      ansible.playbook = 'ansible/dev.yml'
      ansible.inventory_path = 'ansible/vagrant.ini'
    #   ansible.verbose = 'vvvv'
    end
  end
end
