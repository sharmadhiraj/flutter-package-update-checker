from lxml import html
import requests
import yaml


def get_latest_version(package):
    page = requests.get('https://pub.dev/packages/' + package)
    tree = html.fromstring(page.content)
    version_info = tree.xpath('//h2[@class="title"]/text()')[0]
    return version_info.split()[1]


def get_file_name():
    return '/home/dhirajsharma/Drive/Arson/Projects/Flutter/flutter_examples/pubspec.yaml'


def get_packages(file_name):
    yaml_dict = yaml.load(open(file_name), Loader=yaml.FullLoader)
    return yaml_dict['dependencies']


def print_green(text):
    print('\033[94m' + text + '\033[0m')


def print_red(text):
    print('\033[91m' + text + '\033[0m')


def check_update(package, version):
    latest_version = get_latest_version(package)
    latest_version = latest_version.replace("^", "")
    version = version.replace("^", "")
    if latest_version == version:
        print_green(version + " is latest version of " + package + ".")
    else:
        print_red("New version " + latest_version + " is available for " + package + ".")


def main():
    packages = get_packages(get_file_name())
    packages.pop('flutter')
    for package, version in packages.items():
        check_update(package, version)


main()
