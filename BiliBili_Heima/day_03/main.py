from pyecharts.globals import ThemeType

from data_file import Record
from read_file import ReadFile, TextReadFile, JsonReadFile
import json
from pyecharts import charts, options, globals

text_file_data = TextReadFile("d:/test.txt")
json_file_data = JsonReadFile("d://test.json")

text_list_data: list[Record] = text_file_data.read_file()
json_list_data: list[Record] = json_file_data.read_file()

all_data_list: list[Record] = text_list_data + json_list_data

data_dict: dict[int, int] = {}
for record in all_data_list:
    if record.data in data_dict.keys():
        data_dict[record.data] += record.money
        pass
    else:
        data_dict[record.data] = record.money

# 可视化图表开发
bar = charts.Bar(init_opts=options.InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(all_data_list))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=options.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=options.TitleOpts(title="每日销售额"),
)
bar.render("每日销售额.html")
