import paramiko
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template import Template, RequestContext

# Create your views here.


class Login(View):

    def get(self, request):
        """This function render the html"""
        return render(request, 'base.html')


class Status(View):

    def post(self, request):
        """This function is for handling POST request, and will login the server, get the details and render the output."""
        post_data = request.POST
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