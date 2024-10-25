import os
import sys

from organize.handlers.basic import basic_handler_factory

file_types = {
    "images": ["jpg", "png", "gif", "bmp", "tiff", "svg", "webp", "heif", "raw"],
    "programs": ["exe", "app", "bat", "sh", "bin", "jar", "dll", "so", "py", "rb"],
    "text": ["txt", "md", "json", "xml", "html", "log", "ini", "yaml"],
    "ebook": ["epub", "mobi", "pdf", "azw", "ibooks", "fb2", "azw3"],
    "videos": ["mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "3gp", "mpeg"],
    "audio": ["mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "opus", "aiff"],
    "disk_images": ["iso", "img", "dmg", "vmdk", "bin", "vhd", "qcow2", "cdi"],
    "archives": ["zip", "rar", "tar", "gz", "7z"],
    "fonts": ["ttf", "otf", "woff"],
    "web": ["css", "js", "php"],
    "databases": ["sql", "db", "mdb"],
    "tables": ["xls", "xlsx", "csv", "ods"],
    "markup_languages": ["markdown", "latex"],
    "configuration_files": ["conf", "properties"],
    "miscellaneous": ["apk", "ipa", "exe"],
}

def get_sort_handler(options):
    recursive = False
    recurse_option = ""
    if "-r" in options:
        recursive = True
        recurse_option = options[options.index("-r")+1]
    if options[0] == "-x":
        return ""
    else:
        return basic_handler_factory(file_types, recursive, recurse_option)

def sort(path, options):
    handler = get_sort_handler(options)
    with os.scandir(path) as entries:
        for entry in entries:
            handler(entry.path)


def main():
    args = sys.argv
    if len(args) > 1:
        sort(args[1], args[2:])
    else:
        print("Failed, please supply a path a flags")


if __name__ == "__main__":
    main()

