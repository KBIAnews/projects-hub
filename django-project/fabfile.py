from fabric.api import local

# "Universal" KBIA Special Projects Deployment Settings
# You probably don't need to change these.
aws_profile = 'kbia'
stage_domain = 'stage-apps.kbia.org'
deploy_domain = 'apps.kbia.org'

# Project-specific KBIA Special Projects Deployment Settings
# You WILL need to change these.
project_slug = 'kbia_projects_hub' # This will become the slug in the URL. Ex: http://apps.kbia.org/the-slug-here
build_folder = 'baked/kbia_projects_hub' 
# 			For Jekyll projects, build folder is '_site'
#			For Gulp projects, build folder is probably 'build'
#           For Django Bakery projects made from our cookiecutter, build folder is probably 'baked/slug'

def deploy():
	 cmd = "aws s3 cp %s s3://%s/%s --recursive --profile %s" % (build_folder, deploy_domain, project_slug, aws_profile)
	 local(cmd)

def deploy_preview():
	 cmd = "aws s3 cp %s s3://%s/%s --recursive --profile %s" % (build_folder, deploy_domain, project_slug, aws_profile)
	 print(cmd)

def stage():
	 cmd = "aws s3 cp %s s3://%s/%s --recursive --profile %s" % (build_folder, stage_domain, project_slug, aws_profile)
	 local(cmd)

def stage_preview():
	 cmd = "aws s3 cp %s s3://%s/%s --recursive --profile %s" % (build_folder, stage_domain, project_slug, aws_profile)
	 print(cmd)