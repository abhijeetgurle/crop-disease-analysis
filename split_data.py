# divide dataset of images in train and cross validation
import os
import random

# Get the list of directories in current direcotry
dir_list = []
content_list = os.listdir()
for f in content_list:
	if os.path.isdir(f):
		dir_list.append(f)

# Create Test and Validation directory in current directory
if not os.path.exists('Test_dir'):
	os.mkdir('Test_dir')
if not os.path.exists('Val_dir'):
	os.mkdir('Val_dir')	

Test_dir_path = os.path.join(os.getcwd() + '/Test_dir')
Val_dir_path = os.path.join(os.getcwd() + '/Val_dir')

# Scan each class directory for disease classes
for d in dir_list:
	# change directory to disease folder
	os.chdir(d)
	
	# Create Test directory and validation directory and store their paths
	Test_dir_folder_path =  Test_dir_path + '/' + d
	Val_dir_folder_path = Val_dir_path + '/' + d
	if not os.path.exists(Test_dir_folder_path):
		os.mkdir(Test_dir_folder_path)
	if not os.path.exists(Val_dir_folder_path):	
		os.mkdir(Val_dir_folder_path)
	
	# Get the list of images and move 10% to Test_dir and 10% to Val_dir	
	images_list = os.listdir()
	no_of_images = len(images_list)
	no_of_images_in_Test_dir = int(0.1*no_of_images)
	no_of_images_in_Val_dir = int(0.1*no_of_images)
	print("No of images:" + str(no_of_images))
	print("No of images in test:" + str(no_of_images_in_Test_dir))
	print("No of images in valid:" + str(no_of_images_in_Val_dir))

	for i in range(0, no_of_images_in_Test_dir):
		# get random in integer 
		index_to_image = random.randint(0, len(images_list)-1)
		# move image at index to test directory
		os.rename(images_list[index_to_image], Test_dir_folder_path + '/' + images_list[index_to_image])
		no_of_images -= 1
		images_list.pop(index_to_image)

	for i in range(0, no_of_images_in_Val_dir):
		# get random in integer 
		index_to_image = random.randint(0, len(images_list)-1)
		# move image at index to validation directory
		os.rename(images_list[index_to_image], Val_dir_folder_path + '/' + images_list[index_to_image])
		no_of_images -= 1
		images_list.pop(index_to_image)		

	os.chdir('..')


