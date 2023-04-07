import datetime
def handle(request, syscall):
    img_path = request['object-path']
    timestamp = request['input']['timestamp']
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    base = ['home', '%']
    syscall.endorse()
    base.append(str(dt.year))
    year_dir = ':'.join(base)
    syscall.fs_createdir(year_dir)
    base.append(str(dt.month))
    month_dir = ':'.join(base)
    syscall.fs_createdir(month_dir)
    base.append(str(dt.day))
    day_dir = ':'.join(base)
    syscall.fs_createdir(day_dir)
    base.append(str(dt.hour))
    hour_dir = ':'.join(base)
    syscall.fs_createdir(hour_dir)
    base.append(img_path.split(':')[-1])
    index_path = ':'.join(base)
    if syscall.fs_hardlink(img_path, index_path):
        return {'success': True}
    return {'success': False}
