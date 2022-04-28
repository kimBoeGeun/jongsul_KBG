import moisture_driver
import time


class MoistureManager:
    def __init__(self):
        self.moisture = moisture_driver.i2c_moisture()

    def measure(self, time_interval = 0.1, max_cnt = 7, tolerance = 100):
        results = []
        status = (self.moisture.read_word(0x18) & 0x0800)
        cnt = 0

        while cnt < max_cnt:
            if status:
                water = self.moisture.read_word(0x00)
                water = water & 0xFF0F
                masked_water1=(water&0x0F)<<12
                masked_water2=(water>>4)
                final_water=(masked_water1 | masked_water2)>>4
                
                results.append(100-int(final_water))
                time.sleep(time_interval)
                
                while not status:
                    status = (self.moisture.read_word(0x18) & 0x0800)
                    
                cnt += 1

        return results


class ButtonManager:
    def __init__(self):
        pass


if __name__ == "__main__":
    manager = MoistureManager()
    print(manager.measure())
        
