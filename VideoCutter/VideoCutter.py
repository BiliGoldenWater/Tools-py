import os

command = "ffmpeg -y"

working_path = r"E:\Videos\BiliBiliLive\953650-真·凤舞九天-2021-04-12-02-11-连续3金"
src_path = r"录制-953650-20210412-004755-PS5 原神 60p-.flv"
target_path = r"录制-953650-20210412-004755-PS5 原神 60p-afterCut-.flv"

is_cut = True
is_copy = False
is_compression = False
is_nvenc = True

# hh:mm:ss "00:00:00.{}".format(int(0 / fps * 1000))
fps = 60
start_time = "00:00:44.{}".format(int(15 / fps * 1000))
end_time = "00:09:25.{}".format(int(12 / fps * 1000))
target_resolution = "1280*720"
target_bitrate_k = "8192"

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
    command += " -c copy"
if is_compression:
    command += " -b:v {}k -s {}".format(target_bitrate_k, target_resolution)
if is_nvenc:
    command += " -c:v h264_nvenc -c:a copy -b:v {}k".format(target_bitrate_k)

command += " \"{}\"".format(target_path)

os.chdir("{}".format(working_path))
print(command)
# os.system(command)
