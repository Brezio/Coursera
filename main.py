import os
import u_value_module as u_value
import multiprocessing

def process_1(all_files, project_name):
    json_files = os.listdir('json')
    for i in range(all_files):
        if (i % 4 == 0):
            u_value.start_parsing(json_files[i], project_name)

def process_2(all_files, project_name):
    json_files = os.listdir('json')
    for i in range(all_files):
        if (i % 4 == 1):
            u_value.start_parsing(json_files[i], project_name)

def process_3(all_files, project_name):
    json_files = os.listdir('json')
    for i in range(all_files):
        if (i % 4 == 2):
            u_value.start_parsing(json_files[i], project_name)

def process_4(all_files, project_name):
    json_files = os.listdir('json')
    for i in range(all_files):
        if (i % 4 == 3):
            u_value.start_parsing(json_files[i], project_name)

#Make sure that this script is being run as main
if(__name__ != "__main__"):
    print("This script is meant to be run as main and not a module (1).")
    exit(0)

def main():
    os.chdir("Data")
    folders = []
    for i, files in enumerate(os.listdir()):
        print(i, " ", files)
        folders.append(files)
    #Prompt user which folder to do
    user_choice = input("Enter the number of the folder you wish to analyze.")

    #Generate file paths for key items based on user input
    json_file_path = folders[int(user_choice)] + "/json"
    csv_file_path = folders[int(user_choice)] + "/csv"
    image_file_path = folders[int(user_choice)] + "/images"
    ann_file_path = folders[int(user_choice)] + "/ann"
    dir_path = os.path.dirname(__file__)

    #Check to see no files are missing
    # csvs, images = u_value.missing_combination(dir_path, json_file_path, csv_file_path,image_file_path)
    #
    # print(csvs)
    # print(images)
    #
    # if(len(csvs) != 0 or len(images) != 0):
    #     print("Missing CSV's: {}".format(csvs))
    #     print("Missing Images's: {}".format(images))
    #     exit(0)

    project_name = folders[int(user_choice)]
    #Starting process to calculating u_values using files from csv, json, images

    json_path = os.path.join(dir_path, json_file_path.strip())
    os.chdir(project_name)
    all_files = len(os.listdir('json'))

    #Multiprocessing section
    # p1 = multiprocessing.Process(target=process_1, args=(all_files, project_name, ))
    # p2 = multiprocessing.Process(target=process_2, args=(all_files, project_name, ))
    # p3 = multiprocessing.Process(target=process_3, args=(all_files, project_name, ))
    # p4 = multiprocessing.Process(target=process_4, args=(all_files, project_name, ))
    #
    process_1(all_files, project_name)
    process_2(all_files, project_name)
    process_3(all_files, project_name)
    process_4(all_files, project_name)

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()

    print('Done')

    #for json_files in os.listdir('json'):
    #    u_value.start_parsing(json_files, project_name)
main()
