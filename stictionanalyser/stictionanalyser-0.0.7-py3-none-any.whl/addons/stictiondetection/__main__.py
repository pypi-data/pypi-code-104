import os
import sys
import argparse
import subprocess
from getpass import getpass
from urllib.parse import urlparse
from seeq import sdk, spy
from ._copy import copy
from ._utils import sanitize_sdl_url, permissions_defaults
from ._utils import get_datalab_project_id, addon_tool_management

NB_EXTENSIONS = ['widgetsnbextension', 'ipyvuetify', 'ipyvue']
DEPLOYMENT_FOLDER = 'deployment'
DEPLOYMENT_NOTEBOOK = "stiction_detection_master.ipynb"


def install_app(sdl_url_, *, sort_key=None, permissions_group: list = None, permissions_users: list = None):
    """
    Installs Stiction Detection as an Add-on Tool in Seeq Workbench

    Parameters
    ----------
    sdl_url_: str
        URL of the SDL container.
        E.g. https://my.seeq.com/data-lab/6AB49411-917E-44CC-BA19-5EE0F903100C/
    sort_key: str, default None
        A string, typically one character letter. The sort_key determines the
        order in which the Add-on Tools are displayed in the tool panel
    permissions_group: list
        Names of the Seeq groups that will have access to each tool
    permissions_users: list
        Names of Seeq users that will have access to each tool
    Returns
    --------
    -: None
        Stiction Detection will appear as Add-on Tool(s) in Seeq
        Workbench
    """

    sdl_url_ = sanitize_sdl_url(sdl_url_)

    if sort_key is None:
        sort_key = 'a'

    permissions_group, permissions_users = permissions_defaults(permissions_group, permissions_users)

    stiction_details = dict(
        name='Stiction Detection',
        description="Detect oscillations and stiction in the provided data",
        iconClass="fa fa-th",
        targetUrl=f'{sdl_url_}/apps/{DEPLOYMENT_FOLDER}/{DEPLOYMENT_NOTEBOOK}?'
                  f'workbookId={{workbookId}}&worksheetId={{worksheetId}}',
        linkType="window",
        windowDetails="toolbar=0,location=0,left=800,top=400,height=1000,width=1400",
        sortKey=sort_key,
        reuseWindow=True,
        permissions=dict(groups=permissions_group,
                         users=permissions_users)
    )

    copy(des_folder=DEPLOYMENT_FOLDER, src_folder='deployment_notebook',
         overwrite_folder=False, overwrite_contents=True)
    addon_tool_management(stiction_details)


def install_nbextensions():
    for extension in NB_EXTENSIONS:
        subprocess.run(f'jupyter nbextension install --user --py {extension}', cwd=os.path.expanduser('~'), shell=True,
                       check=True)
        subprocess.run(f'jupyter nbextension enable --user --py {extension}', cwd=os.path.expanduser('~'), shell=True,
                       check=True)


def cli_interface():
    """ Installs Stiction Detection as a Seeq Add-on Tool """
    parser = argparse.ArgumentParser(description='Install Stiction Detection as a Seeq Add-on Tool')
    parser.add_argument('--nbextensions_only', action='store_true',
                        help='Only installs the nbextensions without installing or updating the Add-on Tools'
                             'links')
    parser.add_argument('--username', type=str,
                        help='Username or Access Key of Seeq admin user installing the tool(s) ')
    parser.add_argument('--seeq_url', type=str, nargs='?',
                        help="Seeq hostname URL with the format https://my.seeq.com/ or https://my.seeq.com:34216")
    parser.add_argument('--users', type=str, nargs='*', default=[],
                        help="List of the Seeq users to will have access to the Stiction Detection Add-on Tool,"
                             " default: %(default)s")
    parser.add_argument('--groups', type=str, nargs='*', default=['Everyone'],
                        help="List of the Seeq groups to will have access to the Stiction Detection Add-on Tool, "
                             "default: %(default)s")
    return parser.parse_args()


if __name__ == '__main__':

    args = cli_interface()

    if args.nbextensions_only:
        print("\n\nInstalling and enabling nbextensions")
        install_nbextensions()
        sys.exit(0)
    user = args.username
    if user is None:
        user = input("\nAccess Key or Username: ")

    passwd = getpass("Access Key Password: ")
    spy.login(username=user, password=passwd, ignore_ssl_errors=True)
    seeq_url = args.seeq_url
    if seeq_url is None:
        seeq_url = input(f"\n Seeq base URL [{spy.client.host.split('/api')[0]}]: ")
        if seeq_url == '':
            seeq_url = spy.client.host.split('/api')[0]
    url_parsed = urlparse(seeq_url)
    seeq_url_base = f"{url_parsed.scheme}://{url_parsed.netloc}"

    project_id = spy.utils.get_data_lab_project_id()
    sdl_url = f'{seeq_url_base}/data-lab/{project_id}'
    if project_id is None:
        print("\nThe project ID could not be found. Please provide the SDL project URL with the format "
              "https://my.seeq.com/data-lab/6AB49411-917E-44CC-BA19-5EE0F903100C/\n")
        sdl_url = input("Seeq Data Lab project URL: ")
        project_id = get_datalab_project_id(sanitize_sdl_url(sdl_url), sdk.ItemsApi(spy.client))
        if not project_id:
            raise RuntimeError(f'Could not install {args.apps} because the SDL project ID could not be found')
    sdl_url_sanitized = sanitize_sdl_url(sdl_url)

    print(f"\nThe Stiction Detection Tool will be installed on the SDL notebook: {sdl_url_sanitized}\n"
          f"If this is not your intent, you can quit the installation now ")
    print('\n[enter] to continue or type "quit" to exit installation')
    choice = None
    while choice != '' and choice != 'quit':
        choice = input()
        if choice == '':
            print("\n\nInstalling and enabling nbextensions")
            install_nbextensions()
            install_app(sdl_url_sanitized, permissions_group=args.groups, permissions_users=args.users)
        elif choice == 'quit':
            print("\nExited installation")
        else:
            print(f'\nCommand "{choice}" is not valid')
            print('\n[enter] to continue the installation or type "quit" to exit installation')
