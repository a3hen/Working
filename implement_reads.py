# -*- coding: utf-8 -*-
<<<<<<< HEAD
import re
import paramiko
=======

>>>>>>> dev
import yaml
import Connection


def filter_Operation(yaml_name,keyword) :
<<<<<<< HEAD
    if __name__ == '__main__' :
        with open(yaml_name, 'r', encoding='utf-8') as f:
            result = yaml.load(f, yaml.FullLoader)
        for i in range(len(result['Host'])):
            for j in range(len(result['Command'])):
                test_SSH = Connect.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"], result['Host'][i]["User"],result['Host'][i]["Password"], result['Command'][j])
                info = test_SSH.method_processing_data()
                host = result['Host'][i]["IP"]
                if result['Command'][j] == "nmcli connection show":
                    info_old = Connect.filter_data(keyword, info)
                    print(f'{host} 的筛选结果为：{info_old}')
                else:
                    print(result['Host'][i]["IP"]+"的ifconfig信息为：\n"+str(info))
                    print(f'{host} 的ifconfig信息为：{info}')
=======
        with open(yaml_name, 'r', encoding='utf-8') as f:
            result = yaml.load(f, yaml.FullLoader)

        for i in range(len(result['Host'])):
            host = result['Host'][i]["IP"]
            test_SSH = Connection.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"], result['Host'][i]["User"],result['Host'][i]["Password"])
            test_SSH.start_connection()
            for j in range(len(result['Command'])):
                info = test_SSH.stay_connection(result['Command'][j])
                if result['Command'][j] == "nmcli connection show":
                    info_old = Connection.filter_data(keyword, info)
                    print(f'{host} 的筛选结果为：{info_old}')
                else:
                    print(f'{host} 的ifconfig信息为：{info}')
            test_SSH.close_connection()
>>>>>>> dev

if __name__ == '__main__' :
    filter_Operation("test.yaml","ens192")
