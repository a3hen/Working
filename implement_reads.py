# -*- coding: utf-8 -*-
import argparse
import yaml
import connection


def filter_operation(keyword) :

    parser = argparse.ArgumentParser(description="输入yaml文件名")
    parser.add_argument('-apply', '--yaml_name', type=str, help='yaml文件名')
    args = parser.parse_args()
    yaml_name = args.yaml_name


    with open(yaml_name, 'r', encoding='utf-8') as f:
        result = yaml.load(f, yaml.FullLoader)
    for i in range(len(result['Host'])):
    # for i in result['Host'] :
        host = result['Host'][i]["IP"]
        test_SSH = connection.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"], result['Host'][i]["User"],result['Host'][i]["Password"])
        test_SSH.start_connection()
        for j in range(len(result['Command'])):
        # for j in result['Command']:
            info = test_SSH.stay_connection(result['Command'][j])
            if result['Command'][j] == "nmcli connection show":
                info_old = connection.filter_data(keyword, info)
                print(f'{host} 的筛选结果为：{info_old}')
            else:
                print(f'{host} 的ifconfig信息为：{info}')
        test_SSH.close_connection()

if __name__ == '__main__' :
    filter_operation("ens192")
