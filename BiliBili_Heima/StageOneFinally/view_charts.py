import json

from pyecharts import charts, options, globals

f = open("white.txt", "r", encoding="UTF-8")
data_line_list = f.readlines()
f.close()

data_line_list.pop(0)

data_dict = {}
for line in data_line_list:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2].strip())
    try:
        data_dict[year].append([country, gdp])
    except Exception as e:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

sorted_year = sorted(data_dict.keys())

timeline = charts.Timeline({"theme": globals.ThemeType.LIGHT})
for year in sorted_year:
    data_dict[year].sort(key=lambda x: x[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    bar = charts.Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=options.LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=options.TitleOpts(title=f"{year}年GDP")
    )
    timeline.add(bar, str(year))

timeline.render("GDP排行前8")
