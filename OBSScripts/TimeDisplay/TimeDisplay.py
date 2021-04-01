import obspython as obs
import datetime
import time

interval = 10
source_name = ""
strftime = "%Y-%m-%d %H:%M:%S"
prefix = "当前时间: "
suffix = ""
time_offset = 0.00


# ------------------------------------------------------------

def update_text():
    global interval
    global source_name
    global strftime
    global prefix
    global suffix
    global time_offset

    time_stamp = time.time() + (time_offset * 60 * 60)

    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        time_obj = datetime.datetime.fromtimestamp(time_stamp)
        settings = obs.obs_data_create()
        time_str = "格式错误"
        try:
            time_str = "{}{}{}".format(prefix, time_obj.strftime(strftime), suffix)
        except ValueError:
            pass

        obs.obs_data_set_string(settings, "text", time_str)

        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)


def refresh_pressed(props, prop):
    update_text()


# ------------------------------------------------------------

def script_description():
    return "将文本源的内容更新为当前时间。"


def script_defaults(settings):
    obs.obs_data_set_default_double(settings, "interval", 1)
    obs.obs_data_set_default_double(settings, "time_offset", 0)
    obs.obs_data_set_default_string(settings, "source", "")
    obs.obs_data_set_default_string(settings, "prefix", "当前时间: ")
    obs.obs_data_set_default_string(settings, "suffix", "")
    obs.obs_data_set_default_string(settings, "strftime", "%Y-%m-%d %H:%M:%S")


def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "strftime", "时间格式", obs.OBS_TEXT_DEFAULT)

    obs.obs_properties_add_text(props, "prefix", "前缀", obs.OBS_TEXT_DEFAULT)

    obs.obs_properties_add_text(props, "suffix", "后缀", obs.OBS_TEXT_DEFAULT)

    obs.obs_properties_add_float(props, "interval", "刷新间隔 (秒)", 0, 3600, 0.5)

    obs.obs_properties_add_float(props, "time_offset", "时间偏移 (小时)", -24, 24, 1)

    p = obs.obs_properties_add_list(props, "source", "文本源", obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_id(source)
            if source_id.startswith("text"):
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "刷新", refresh_pressed)
    return props


def script_unload():
    obs.timer_remove(update_text)


def script_update(settings):
    global interval
    global source_name
    global strftime
    global prefix
    global suffix
    global time_offset

    interval = obs.obs_data_get_double(settings, "interval")
    source_name = obs.obs_data_get_string(settings, "source")
    strftime = obs.obs_data_get_string(settings, "strftime")
    prefix = obs.obs_data_get_string(settings, "prefix")
    suffix = obs.obs_data_get_string(settings, "suffix")
    time_offset = obs.obs_data_get_double(settings, "time_offset")

    obs.timer_remove(update_text)

    if source_name != "":
        obs.timer_add(update_text, int(max(interval * 1000, 1)))
