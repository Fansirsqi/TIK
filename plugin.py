import androguard
import os


def got_all_apk_file(project):
    apk_files = []

    for root, dirs, files in os.walk(project):
        for file in files:
            if file.endswith('.apk'):
                apk_files.append(os.path.join(root, file))

    return apk_files


if __name__ == '__main__':
    project = 'C:/Users/fansir/Documents/TI_miui_PHOENIX_V13.0.2.1.47.DEV_d75e8be0ee_12.0_2'
    file_list = got_all_apk_file(project)
    for i in file_list:
        print(i)
