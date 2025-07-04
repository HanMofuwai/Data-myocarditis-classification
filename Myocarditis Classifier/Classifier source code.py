import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        root.geometry('400x300')  # 窗口大小
        root.title('Classifier')  # 标题

        # 创建输入控件
        tk.Label(root, text="BMI:").pack()
        self.bmi_entry = tk.Entry(root)
        self.bmi_entry.pack()

        tk.Label(root, text="Age onset:").pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        # 创建下拉菜单用于类别变量
        tk.Label(root, text="Family history:").pack()
        self.var_a = tk.StringVar()
        self.a_combobox = ttk.Combobox(root, textvariable=self.var_a, 
                                     values=["Present", "Absent"], state="readonly")
        self.a_combobox.pack()
        self.a_combobox.set("Present")  # 默认值

        tk.Label(root, text="Proviral infection:").pack()
        self.var_b = tk.StringVar()
        self.b_combobox = ttk.Combobox(root, textvariable=self.var_b, 
                                     values=["Present", "Absent"], state="readonly")
        self.b_combobox.pack()
        self.b_combobox.set("Present")  # 默认值

        # 分类按钮
        self.button = tk.Button(root, text='Classify', command=self.classify)
        self.button.pack(pady=10)

        # 结果显示
        self.result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))
        self.result_label.pack()

    def classify(self):
        try:
            bmi = float(self.bmi_entry.get())
            age = float(self.age_entry.get())
            var_a = self.var_a.get().lower()  # 转换为小写方便比较
            var_b = self.var_b.get().lower()
        except ValueError:
            self.result_label.config(text="Please enter valid numbers for BMI and Age!")
            return

        # 实现分类逻辑
        if bmi < 20:
            result = "PG3"
        elif bmi >= 20 and var_a == "present":
            result = "PG1"
        elif (bmi >= 20 and var_a == "absent" 
              and age < 45 and var_b == "absent"):
            result = "PG1"
        else:
            result = "PG2"

        self.result_label.config(text=f"Classification Result: {result}")

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()