import os

command = "ffmpeg -y"

src_path = r"E:\Videos\BiliBiliLive\live_865267_9146410-2021-03-13-23-30-诶嘿.flv"
target_path = r"E:\Videos\BiliBiliLive\live_865267_9146410-2021-03-13-23-30-诶嘿.mp4"

# hh:mm:ss
is_cut = False
is_copy = True
is_compression = False
is_nvenc = True

start_time = "00:00:00"
end_time = "00:00:00"
target_resolution = "1280*720"
target_bitrate_k = "1024"

if is_compression:
    is_copy = False
if is_copy:
    is_nvenc = False

src_path = src_path.replace("\"", "").replace("'", "")
target_path = target_path.replace("\"", "").replace("'", "")

command += " -i \"{}\"".format(src_path)

if is_cut:
    command += " -ss {} -to {}".format(start_time, end_time)
if is_copy:
    command += " -vcodec copy -acodec copy"
if is_compression:
    command += " -b:v {}k -s {}".format(target_bitrate_k, target_resolution)
if is_nvenc:
    command += " -c:v h264_nvenc"

command += " \"{}\"".format(target_path)

# os.system(command)
print(command)
