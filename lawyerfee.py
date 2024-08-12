from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# 设置窗口大小，便于在桌面测试
Window.size = (300, 500)


class LawyerFeeCalculator(BoxLayout):
    def calculate_fee(self):
        try:
            part1_cacunum = float(self.ids.input_box.text)
            part1_c = int(part1_cacunum)
            if part1_c < 100000:
                part1_result1 = 3000
                part1_result2 = 10000
            elif 100000 <= part1_c < 500000:
                part1_result1 = (part1_c - 100000) * 0.06 + 3000
                part1_result2 = (part1_c - 100000) * 0.08 + 10000
            elif 500000 <= part1_c < 5000000:
                part1_result1 = (part1_c - 500000) * 0.04 + 27000
                # 0.3w + 40w * 0.06 (27,000，2.7w)
                part1_result2 = (part1_c - 500000) * 0.06 + 42000
                # 1w + 40w * 0.08 (3.2w)
            elif 5000000 <= part1_c < 20000000:
                part1_result1 = (part1_c - 5000000) * 0.02 + 207000
                # 2.7w + 450w * 0.04
                part1_result2 = (part1_c - 5000000) * 0.04 + 312000
                # 4.2w + 450w * 0.06
            elif 20000000 <= part1_c < 100000000:
                part1_result1 = (part1_c - 20000000) * 0.01 + 507000
                # 20.7w + 1500w * 0.02
                part1_result2 = (part1_c - 20000000) * 0.02 + 912000
                # 31.2w + 1500w * 0.04
            elif part1_c >= 100000000:
                part1_result1 = (part1_c - 100000000) * 0.005 + 1307000
                # 50.7w + 8000w * 0.01
                part1_result2 = (part1_c - 100000000) * 0.01 + 2512000
                # 91.2w + 8000w * 0.02

            else:
                part1_result1 = 0
                part1_result2 = 0

            self.ids.output_label.text = ("案件金额：\n" + str(part1_c) + "元\n\n律师费：\n"
                                          + str(int(part1_result1)) + "元 - " + str(int(part1_result2)) + "元\n\n")
        except ValueError:
            # 如果输入无法转换为浮点数，则显示错误信息
            self.ids.output_label.text = "请输入有效的数字"


class LawyerFeeApp(App):
    def build(self):
        return LawyerFeeCalculator()


if __name__ == '__main__':
    LawyerFeeApp().run()
