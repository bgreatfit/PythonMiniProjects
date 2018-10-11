import os



submission_dir = 'completed_assignments'
dir_list = os.listdir(submission_dir)
file_tup = {}
for directory in dir_list:
    file_list = list(os.listdir(os.path.join(submission_dir, directory)))
    if len(file_list) != 0:
        print(file_list[0])
        file_tup[directory] = file_list[0]

