# -*- coding: utf-8 -*-

import yaml
import Connection


def filter_Operation(yaml_name,keyword) :
    if __name__ == '__main__' :
        with open(yaml_name, 'r', encoding='utf-8') as f:
            result = yaml.load(f, yaml.FullLoader)
    for i in range(len(result['Host'])):
        for j in range(len(result['Command'])):
            test_SSH = Connection.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"], result['Host'][i]["User"],result['Host'][i]["Password"], result['Command'][j])
            info = test_SSH.method_processing_data()
            host = result['Host'][i]["IP"]
            if result['Command'][j] == "nmcli connection show":
                info_old = Connection.filter_data(keyword, info)
                print(f'{host} 的筛选结果为：{info_old}')
            else:
                print(result['Host'][i]["IP"]+"的ifconfig信息为：\n"+str(info))
                print(f'{host} 的ifconfig信息为：{info}')

if __name__ == '__main__' :
    filter_Operation("test.yaml","ens192")
