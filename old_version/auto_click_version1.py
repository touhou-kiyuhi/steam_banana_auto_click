import win32gui, win32con
import pyautogui
import time

class Banana_window:
    def __init__(self, times):
        # 螢幕大小
        screen_x, screen_y = pyautogui.size()
        print(f"螢幕大小，x:{screen_x}, x: {screen_y}")
        # 取得視窗句柄
        self.handle = win32gui.FindWindow(None, "Banana")
        # top: [1]
        # bottom: [3]
        # left: [0]
        # right: [2]
        # 取得視窗左、上、右、下邊界值
        self.handleDetail = win32gui.GetWindowRect(self.handle)
        print(self.handleDetail)
        print("the maximaized window detail:\ntop: {}, bottom: {}, left: {}, right: {}"
                .format(self.handleDetail[1], self.handleDetail[3], 
                        self.handleDetail[0], self.handleDetail[2]))
        # 滑鼠x、y軸
        self.cursor_x = screen_x // 2 
        self.cursor_y = screen_y // 2

        self.times = times
        self.count = 0

    def window_settings(self):
        # 視窗最大化
        win32gui.ShowWindow(self.handle, win32con.SW_MAXIMIZE)
        # 視窗前置最上層
        win32gui.SetForegroundWindow(self.handle)

    def cursor_control(self):
        # 移動
        pyautogui.moveTo(self.cursor_x, self.cursor_y, 1)
        for i in range(self.times):
            x, y = pyautogui.position()
            if self.cursor_x == x < self.cursor_x + 50 or self.cursor_y - 100 < y < self.cursor_y + 50:
                # 點擊
                pyautogui.click()
                self.count += 1 
            else:
                print("中止")
                print(f"此次運行共點擊: {self.count}")
                break
        print(f"此次運行共點擊: {self.count}")

def main(times):
    bw = Banana_window(times)
    bw.window_settings()
    bw.cursor_control()
    pass

if __name__ == '__main__':
    # 期望點擊次數
    times = 10000

    main(times)