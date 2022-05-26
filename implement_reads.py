# -*- coding: utf-8 -*-

import yaml
import Connection


def filter_Operation(yaml_name,keyword) :
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

if __name__ == '__main__' :
    filter_Operation("test.yaml","ens192")
