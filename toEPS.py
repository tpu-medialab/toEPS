import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def window():
    # ウィンドウフォーム
    form1 = tk.Tk()
    form1.geometry("800x100")
    form1.title(u"folder_name")

    # フォームのテキスト
    label5 = tk.Label(form1, text='画像フォルダ')
    label5.grid(row=5, column=1, padx=1, pady=1, sticky=tk.W)

    # ファイル名のテキスト
    textbox5 = tk.Entry(form1, width=60)
    textbox5.grid(row=5, column=2, pady=1, sticky=tk.W)

    # フォームのボタン
    button2 = tk.Button(form1, text='参照', command=lambda: file_path(textbox5))
    button2.grid(row=5, column=3, ipadx=20)
    button2.bind('<Return>', lambda event: file_path(textbox5))

    button3 = tk.Button(form1, text='実行', command=lambda: submit(textbox5))
    button3.grid(row=6, column=2)

    # 作成後のパス
    def file_path(textbox):
        v_iDir = os.path.abspath(os.path.dirname(__file__))
        if v_path := filedialog.askdirectory(initialdir=v_iDir):
            textbox.delete(0, tk.END)
            textbox.insert(0, v_path)

    def submit(textbox):
        global folder_path
        folder_path = textbox.get()
        if folder_path:
            form1.destroy()
            edit()
        else:
            messagebox.showerror('警告', '正しい値を入力してください')

    form1.mainloop()

# フォルダ内の全てのファイルを取得
def edit():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            try:
                img = Image.open(file_path)
                img = img.convert('RGB')
                eps_path = os.path.splitext(file_path)[0] + '.eps'
                img.save(eps_path, 'EPS')
                print(f"Converted {filename} to EPS format.")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

def main():
    window()

if __name__ == "__main__":
    main()
