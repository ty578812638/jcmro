#!/usr/sbin/python3
import gitlab
import time
import os

git_url = 'http://192.168.1.17/'
git_token = 'XbEURKtB1m2AkgTyyH6K'
project_root = '/root/flow-web'


class get_gitlab:

    def __init__(self):
        self.url = git_url
        self.token = git_token
        self.root_path = project_root

    # 登陆
    def login_gitlab(self):
        gl = gitlab.Gitlab(self.url, self.token)
        return gl

    # 用项目id获取项目
    def get_project_id(self, id):
        gl = self.login_gitlab()
        project = gl.projects.get(id)
        return project

    # 由于是递归方式下载的所以要先创建项目相应目录
    def create_dir(self, dir_name):
        if not os.path.isdir(dir_name):
            print("\033[0;32;40m开始创建目录: \033[0m{0}".format(dir_name))
            os.makedirs(dir_name)
            time.sleep(0.1)

    def start_get(self):
        project = self.get_project_id(6)
        info = project.repository_tree(all=True, recursive=True, as_list=True)
        file_list = []
        if not os.path.isdir(self.root_path):
            os.makedirs(self.root_path)
        os.chdir(self.root_path)
        # 调用创建目录的函数并生成文件名列表
        for info_dir in range(len(info)):
            if info[info_dir]['type'] == 'tree':
                dir_name = info[info_dir]['path']
                self.create_dir(dir_name)
            else:
                file_name = info[info_dir]['path']
                file_list.append(file_name)
        for info_file in range(len(file_list)):
            # 开始下载
            getf = project.files.get(file_path=file_list[info_file], ref='master')
            content = getf.decode()
            with open(file_list[info_file], 'wb') as code:
                print("\033[0;32;40m开始下载文件: \033[0m{0}".format(file_list[info_file]))
                code.write(content)


st_init = get_gitlab()
st_init.start_get()