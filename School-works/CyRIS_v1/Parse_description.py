import yaml
from entities import Host, Guest, CloneGuest, CloneSubnetwork, CloneInstance, CloneHost, CloneSetting
from storyboard import Storyboard
BASEIMG_ROOT_PASSWD = "theroot"
hosts = []
guests = []

def get_host_object(host_id):
        for host in hosts:
            if host_id == host.getHostId():
                return host
        return None

def parse_description(filename):
        
        try:
            with open(filename, "r") as f:
                doc = yaml.load(f)
        except yaml.YAMLError as exc:
            print ("* ERROR: cyris: Issue with the cyber range description file: ", exc)
            return

        # for each playbook in the training description
        for element in doc:
            if "host_settings" in element.keys():
                for i,h in enumerate(element["host_settings"]):
                    if i == 0:
                        global MSTNODE_ACCOUNT
                        global MSTNODE_MGMT_ADDR
                        MSTNODE_ACCOUNT = h["account"]
                        MSTNODE_MGMT_ADDR = h["mgmt_addr"]
                    host = Host(h["id"], h["virbr_addr"], h["mgmt_addr"], h["account"])
                    hosts.append(host)
        
            if "guest_settings" in element.keys():
                for i,g in enumerate(element["guest_settings"]):
                    # If user specifies ip_addr for the guest.
                    if "ip_addr" in g.keys():
                        ip_addr = g["ip_addr"]
                    # Else, CyRIS generates ip_addr for the guest using its own rules as below.
                    else:
                        # Assign last bit of IP addr for the guest, which is the sum of 100 and the guest's i.
                        #last_bit = add_basevm_ipaddr(100 + i)
                        # Generate IP addr for the guest, which is 192.168.122.{last_bit}.
                        #ip_addr = "192.168.122.{0}".format(last_bit)
                        ip_addr = "192.168.122.101"
                    # If user specifies tasks for the guest.
                    if "tasks" in g.keys():
                        tasks = g["tasks"]
                    else:
                        tasks = []
                    guest = Guest(g["id"], ip_addr, BASEIMG_ROOT_PASSWD, g["basevm_host"], g["basevm_config_file"], g["basevm_type"], "", tasks)
                    guests.append(guest)

        if "clone_settings" in element.keys():
            range_id = element["clone_settings"][0]["range_id"]
            #range_id = range_id # Save for future reference
            clone_host_list = []

            for host in element["clone_settings"][0]["hosts"]:
                # The 'host_id' of 'host' may contain a list of ids,
                # so we split the list if needed
                host_id_str = host["host_id"]
                host_id_list = []
                if "," in host_id_str:
                    host_id_list = host_id_str.replace(" ","").split(",")
                else:
                    host_id_list.append(host_id_str)
                for host_id in host_id_list:
                    instance_num = host["instance_number"]
                    # set network topology type
                    nw_type = host["topology"][0]["type"]
                    instance_list = []
                    for i in range(1, instance_num+1):
                        # Since each instance reuse the information of the guest, it's important to 
                        # recreate a clone_guest_list and clone_subnw_list  when creating a new instance.
                        clone_subnw_list = []
                        for subnetwork in host["topology"][0]["networks"]:
                            name = subnetwork["name"]
                            members = subnetwork["members"]
                            if "gateway" in subnetwork.keys():
                                gateway = subnetwork["gateway"]
                            else:
                                gateway = ""
                            clone_subnetwork = CloneSubnetwork(name, members, gateway)
                            clone_subnw_list.append(clone_subnetwork)
                        clone_guest_list = []
                        for guest in host["guests"]:
                            guest_id = guest["guest_id"]
                            number = guest["number"]
                            fw_rules = []
                            if Storyboard.FORWARDING_RULES in guest.keys():
                                has_fw_setup = True
                                for rule in guest[Storyboard.FORWARDING_RULES]:
                                    fw_rules.append(rule[Storyboard.RULE])
                            else:
                                has_fw_setup = False
                            if "entry_point" in guest.keys():
                                is_entry_point = True
                            else:
                                is_entry_point = False
                            # Create a list of clone_guest with size=number
                            for k in range(1, number+1):
                                clone_guest = CloneGuest(guest_id, k, has_fw_setup, fw_rules, is_entry_point)
                                clone_guest_list.append(clone_guest)
                        instance = CloneInstance(i, clone_guest_list, clone_subnw_list)
                        instance_list.append(instance)

                    # Find host with same id in the hosts list and use it to initialize the CloneHost object
                    # We use a new object 'actual_host' because the object 'host' above may contain a list of host ids
                    actual_host = get_host_object(host_id)
                    clone_host = CloneHost(actual_host, instance_list)
                    clone_host_list.append(clone_host)
            clone_setting = CloneSetting(range_id, nw_type, clone_host_list)
            

        # Set basevm_name for guests
        for guest in guests:
            basevm_name = "{0}_cr{1}_base".format(guest.getGuestId(), clone_setting.getRangeId())
            guest.setBasevmName(basevm_name)
            print(basevm_name)
        print(host)
        
fileName = "basic.yml"
parse_description(fileName)