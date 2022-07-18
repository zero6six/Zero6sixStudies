import os
import time

originalFile = r"E:\Develop\project\gitcode\mcstaralliance\ZenScript\20220704"
copyFile = r'E:\minecraft\forge\[1.12.2]星域世界-13.0.0\.minecraft'


monitorFile = os.path.join(copyFile, r'scripts\CraftTweaker\remove.zs')
command = f'xcopy {originalFile} {copyFile} /E /Y'

times = 0
while True:
    print("正在持续监控文件。")
    if os.path.exists(monitorFile) == False:
        print("文件已被删除，正在复制！")
        os.system(command)
    times += 1
    print(f'这是第 {times} 次循环')
    time.sleep(10)
    