# 课程表查询程序
def course_query():
    # ===================== 可修改区域 START =====================
    # 1. 此处定义课程表，键为星期（周一至周五），值为对应课程列表（按第1-4节课顺序排列）
    #    如需修改课程名称：直接替换列表中的字符串即可
    #    如需修改节数：增加/删除列表中的元素（保持与查询逻辑匹配即可，当前默认4节课）
    course_table = {
        "周一": ["3Dmax", "数据可视化", "Mysql", "Python"],
        "周二": ["3Dmax", "数据可视化", "Mysql", "Python"],
        "周三": ["3Dmax", "数据可视化", "Mysql", "Python"],
        "周四": ["3Dmax", "数据可视化", "Mysql", "Python"],
        "周五": ["3Dmax", "数据可视化", "Mysql", "班会课"]  # 周五最后一节为班会课
    }
    # ===================== 可修改区域 END =====================

    # 获取用户输入
    user_input = input("请输入要查询的星期（如：周一）：")

    # 判断输入是否有效
    if user_input in course_table:
        # 输出当天课程，按节数清晰展示
        print(f"\n{user_input}的课程安排如下：")
        for index, course in enumerate(course_table[user_input], start=1):
            print(f"第{index}节课：{course}")
    else:
        # 输入错误提示
        print("输入格式不对，请输入周一到周五")

# 运行程序
if __name__ == "__main__":
    course_query()