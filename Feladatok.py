#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():
        def __init__(self):
        # tégla
                self.ev3 = EV3Brick()
        # motorok
                self.jm = Motor(Port.B)
                self.bm = Motor(Port.C)
                self.km = Motor(Port.A)
        # szenzorok
                self.cs = ColorSensor(Port.S3)
                self.ts = TouchSensor(Port.S1)
                self.gs = GyroSensor(Port.S2)
                self.us = UltrasonicSensor(Port.S4)
                #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
                self.robot = DriveBase(self.jm, self.bm, 55, 115)
                self.ido = StopWatch()
                self.data = DataLog(name='adatok', timestamp=False, extension='csv')
                #self.data = DataLog('time','angle',name='dataLog', timestamp=False, extension='txt',append=True)
        
        def feladat(self):
                self.data.log('Hello','Világ')  
                print(self.data)
        def vonalak(self):
                self.vonalHossza()
        def vonalHossza(self):
                hosszok = []
                db = 5
                self.robot.drive(100,0)
                self.data.log("Hány db vonal:")
                self.data.log(db)
                for vonalakSzama in range(db):
                        vege = False
                        fekete = False
                        self.robot.drive(100,0)
                        while not vege:
                                if self.cs.reflection() < (74+10)/2-20 and not fekete:
                                        fekete = True
                                        self.ido.reset()
                                if fekete and self.cs.reflection() > (74+10)/2-10:
                                        vege = True
                                        hossz = self.ido.time()
                                        hosszok.append(hossz)
                        self.robot.stop(Stop.BRAKE)
                        print(hossz)
                print(hosszok)
                self.data.log('Hosszak:')
                self.data.log(hosszok)
                return hosszok
                #self.data.log(hosszok)
               # print(self.data)
