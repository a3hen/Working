import re
import paramiko
import yaml
import Connect

class Filter_operation :
    def __init__(self,yaml_name,keyword):
        self.yaml_name = yaml_name
        self.keyword = keyword

    def Main(self) :
        if __name__ == '__main__' :
            with open(self.yaml_name, 'r', encoding='utf-8') as f:
                result = yaml.load(f, yaml.FullLoader)

                for i in range(len(result['Host'])):
                    for j in range(len(result['Command'])):
                        if result['Command'][j] == "nmcli connection show":
                            test_SSH = Connect.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"],result['Host'][i]["User"], result['Host'][i]["Password"],result['Command'][j])
                            info = test_SSH.method_processing_data()
                            info_old = Connect.filter_data(self.keyword, info)
                            print(result['Host'][i]["IP"]+"的筛选结果为：\n"+str(info_old))
                        else:
                            test_SSH = Connect.Ssh(result['Host'][i]["IP"], result['Host'][i]["Port"],result['Host'][i]["User"], result['Host'][i]["Password"],result['Command'][j])
                            info = test_SSH.method_processing_data()
                            print(result['Host'][i]["IP"]+"的ifconfig信息为：\n"+str(info))

if __name__ == '__main__' :
    test = Filter_operation("test.yaml","ens192")
    test.main()

