from helper.createdesktop import create_desktop_entry

from helper.moveshare import copy_to_local_share

from helper.movetoapplication import copy_to_applications

from helper.BashRunner import RunBash

print('starting setup...')
print('copying files...')
iconspath = copy_to_local_share(app_name='Corkscrew',file='src/storage/res/icons')

scripts = copy_to_local_share(app_name='Corkscrew',file='src/sh')


icon = str(iconspath/'corkscrew.png')

print('creating entries...')

fullscreen = create_desktop_entry(
    name='Run in fullscreen',
    file_name='fullscreen',
    exec_command='wine %f -screen-fullscreen 1',
    icon=icon,
    output_path='src/commands',
    mime_types=['application/x-msdownload']
)

windowed = create_desktop_entry(
    name='Run in windowed',
    file_name='windowed',
    exec_command='wine %f -screen-fullscreen 0',
    icon=icon,
    output_path='src/commands',
    mime_types=['application/x-msdownload']
)

runexe = create_desktop_entry(
    name='Run exe',
    file_name='runapp',
    exec_command='wine %f',
    icon=icon,
    output_path='src/commands',
    mime_types=['application/x-msdownload']
)

print('copying once more...')

copy_to_applications(str(fullscreen))
copy_to_applications(str(windowed))
pa = copy_to_applications(str(runexe))


print('setting defualt handler...')

RunBash(str(scripts/'def.sh'),[pa])


print('setup complete!!!')
