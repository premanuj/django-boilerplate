import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Rename django's project environment"

    def add_arguments(self, parser):
        parser.add_argument('new_environment', type=str, help="The new Django environment (dev, prod)")
    
    def handle(self, *args, **kwargs):
        new_environment = kwargs.get('new_environment')
        files_to_rename = 'manage.py'

        project_name = ""
        env_line = ""
        for path, folders, _  in os.walk(os.getcwd()):
            if 'settings' in folders:
                project_name = path.split('/')[-1]
                break

        with open(files_to_rename, 'r') as file:
            filelines = file.readlines()
        for line in filelines:
            if 'os.environ.setdefault' in line:
                env_line = line 
                break
        env_setting = env_line.split(',')[-1].replace(')', '').replace('\n','')
        env_lines = ''.join(filelines)
        env_lines= env_lines.replace(f'{env_setting}', f" '{project_name}.settings.{new_environment}'")
        with open(files_to_rename, 'w') as file:
            file.write(env_lines)
                
        self.stdout.write(self.style.SUCCESS("Project environment has been changed to %s" % new_environment ))
