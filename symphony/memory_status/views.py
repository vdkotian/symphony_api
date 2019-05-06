import paramiko
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template import Template, RequestContext

# Create your views here.


class Login(View):

    def get(self, request):
        return render(request, 'base.html')


class Status(View):

    def post(self, request):
        print("Hello", request)
        post_data = request.POST
        print(post_data)
        with paramiko.SSHClient() as ssh:
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(post_data['host'], username=post_data['username'],
                        password=post_data['password'],port=post_data.get('port',22))
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("vmstat -s")
            data = ''
            for line in ssh_stdout.readlines():
                data += line
        print(data)
        return JsonResponse({"data": data})