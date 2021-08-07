# Here are some rules that will make our lives easier

# FOLDER STRUCTURE
### [model-name]
#### Ex:
	- Model Post:
		- post/
			- html file
			- html file
		
	- Model UniversitySystem:
		- uni-system/
			- html file
			- html file

# HTML FILES
### [model-name]-[action].html
#### Ex:
	- Model Post:
		- post-create.html
		- post-update.html
		- and so on
		
	- Model UniversitySystem:
		- uni-system-update.html
		- uni-system-all.html
		
# URL ROUTES
### [Model-Name]/[action]/[*args]/[**kwargs]
#### Ex:
	- Model UniversitySystem:
		- Uni-System/create/
		- Uni-System/edit/<int:id>/
		- Uni-System/delete/<int:id>/
		- and so on
		
# URL NAMES
### [model-name]-[action]-[*args]-[**kwargs]
#### Ex:
	- Model Post:
		- post-create
		- post-update
		- and so on
		
	- Model UniversitySystem:
		- uni-system-edit
		- uni-system-all
		
# VIEW NAMES
### [model_name]_[action]
#### Ex:
	- Model Post:
		- post_create
		- post_update
		- and so on
		
	- Model UniversitySystem:
		- uni_system_edit
		- uni_system_all