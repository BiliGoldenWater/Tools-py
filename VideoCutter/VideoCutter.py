import os

command = "ffmpeg -y"

working_path = r"E:\Videos\BiliBiliLive\BililiveRecorder\7953876-宴宁ccccc"
src_path = r"录制-7953876-20210321-003348-来了 今日无头-.flv"
target_path = r"录制-7953876-20210321-003348-来了 今日无头-720p-1Mbps.mp4"

is_cut = False
is_copy = True
is_compression = True
is_nvenc = True

# hh:mm:ss "00:00:00"
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
    command += " -c copy"
if is_compression:
    command += " -b:v {}k -s {}".format(target_bitrate_k, target_resolution)
if is_nvenc:
    command += " -c:v h264_nvenc -c:a copy -b:v {}k".format(target_bitrate_k)

command += " \"{}\"".format(target_path)

os.chdir("{}".format(working_path))
print(command)
os.system(command)
