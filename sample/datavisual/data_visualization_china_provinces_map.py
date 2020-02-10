# coding:utf-8
# [转载](https://www.cnblogs.com/qi-yuan-008/p/12025305.html)
from pyecharts import options as opts
from pyecharts.charts import Map

# 用于测试的例子，部分取自 Faker ，也就是 from pyecharts.faker import Faker
provinces = ["广东", "北京", "上海", "辽宁", "湖南", "四川", "西藏"]
value = [300, 100, 2000, 800, 10000, 400, 5000]


# 连续性数据显示，不同颜色不同省份
def map_visualmap() -> Map:
    c = (
        Map()
            .add("", [list(z) for z in zip(provinces, value)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国省级地图"),
            visualmap_opts=opts.VisualMapOpts(max_=2000),
        )
    )
    return c


if __name__ == '__main__':
    city_ = map_visualmap()
    city_.render(path="中国省级地图.html")
