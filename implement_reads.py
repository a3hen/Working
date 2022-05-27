# -*- coding: utf-8 -*-
import argparse
import yaml
import connection


def filter_operation(keyword) :

    parser = argparse.ArgumentParser(description="输入yaml文件名")
    subparser = parser.add_subparsers(help="子命令帮助")
    parser_a = subparser.add_parser('apply',help="apply help")
    parser_a.add_argument('yaml_name',type=str,help='yaml name')
    args = parser.parse_args()
    yaml_name = args.yaml_name


    with open(yaml_name, 'r', encoding='utf-8') as f:
        result = yaml.load(f, yaml.FullLoader)
    for i in result['Host'] :
        host = i["IP"]
        test_SSH = connection.Ssh(i["IP"],i["Port"],i["User"],i["Password"])
        test_SSH.start_connection()
        for j in result['Command'] :
            info = test_SSH.stay_connection(j)
            if j == 'nmcli connection show':
                info_old = connection.filter_data(keyword, info)
                print(f'{host} 的ifconfig信息为：{info_old}')
            else:
                print(f'{host} 的free -m的信息为: {info}')
        test_SSH.close_connection()

if __name__ == '__main__' :
    filter_operation("ens192")
