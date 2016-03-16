import glob
import os
import yaml

for file_path in glob.glob('./bootcamps/*/data.yml'):
    with open(file_path) as stream:
        data = yaml.load(stream)
        for key in [
            'status', 'physical_address', 'google_search_volume',
                'founder_name', 'active_students']:
            del data[key]
    with open(file_path, 'wb') as stream:
        yaml.safe_dump(data, stream, default_flow_style=False)


for file_path in glob.glob('./bootcamps/*/programs/*/highlights.md'):
    os.remove(file_path)

for file_path in glob.glob('./bootcamps/*/programs/*/projects.yml'):
    os.remove(file_path)

for file_path in glob.glob('./bootcamps/*/programs/*/payment_options.md'):
    os.remove(file_path)

for file_path in glob.glob('./bootcamps/*/programs/*/data.yml'):
    with open(file_path) as stream:
        data = yaml.load(stream)
        for key in [
            'acceptance_rate', 'class_size', 'full_slug',
                'hiring_partners', 'hours_per_week', 'ideal_for',
                'job_placement_rate', 'number_of_graduates',
                'status', 'student_teacher_ratio', 'syllabus']:
            del data[key]
    with open(file_path, 'wb') as stream:
        yaml.safe_dump(data, stream, default_flow_style=False)
