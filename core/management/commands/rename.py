import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Rename django's project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help="The new Django project name")
    
    def handle(self, *args, **kwargs):
        new_project_name = kwargs.get('new_project_name')
        
        #Logic to rename project
        folder_to_rename = ""
        for path, folders, _  in os.walk(os.getcwd()):
            if 'settings' in folders:
                folder_to_rename = path.split('/')[-1]
                break
        files_to_rename = [f'{folder_to_rename}/settings/base.py',f'{folder_to_rename}/wsgi.py', 'manage.py']

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            
            filedata = filedata.replace(f'{folder_to_rename}', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)
                
        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS("Project has been renamed to %s" % new_project_name ))
