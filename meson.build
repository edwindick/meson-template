# meson.build - Entry point of build system.

# Project function goes here.

###############################################################################
#       Build Scripts

python = find_program('python3', 'python', required: true)

copy_to = meson.current_source_dir() / 'scripts/copy_to.py'
recursive_search = meson.current_source_dir() / 'scripts/recursive_search.py'

###############################################################################
#       Subdirectories

project_deps = []
subdir('lib') # lib/meson.build sets project_deps array.

project_inc = include_directories('./include')

subdir('src')