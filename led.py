 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
   
import time
import pigpio #pigpioライブラリをインポートする
   
pi = pigpio.pi() #GPIOにアクセスするためのインスタンスを作成します
pi.set_mode(18, pigpio.OUTPUT) #GPIOのモードを設定します他にINPUTとかある。18はGPIO18の18番です。
   
try:
    while True:
        pi.write(18, 1) #GPIO18番のレベルをHIGHにします
        time.sleep(0.5)
        pi.write(18, 0) #GPIO18番のレベルをLOWにします
        time.sleep(0.5)
except KeyboardInterrupt:
      print('KeyboardInterrupt')
      pi.write(18.0)
      pi.stop()