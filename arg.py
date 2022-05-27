# -*- coding: utf-8 -*-
import argparse
import math


def get_yaml ():

    parser = argparse.ArgumentParser(description="输入yaml文件名")
    parser.add_argument('-apply','--yaml_name',type=str,help='yaml文件名')
    args = parser.parse_args()
    return args.yaml_name


if __name__ == '__main__' :
    print(get_yaml())


