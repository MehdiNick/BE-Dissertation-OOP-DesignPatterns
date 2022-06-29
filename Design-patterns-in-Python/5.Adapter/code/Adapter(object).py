from abc import ABC, abstractmethod
import math
from random import randint


class TargetSMS(ABC):
    @abstractmethod
    def SendSms(self, number):
        pass


class SoapSms():
    def sendSmsBySoapByNumber(self, number):
        print(f"sending {randint(1000,9999)} to {number} ")


class SMSAdapter(TargetSMS):
    def SendSms(self, number):
        self.smsAproach = SoapSms()
        self.smsAproach.sendSmsBySoapByNumber(number)


class APPLogin:
    # ....
    # some codes here
    def __init__(self):
        self.SMSAdapter = SMSAdapter()
        self.SMSAdapter.SendSms("09305667042")

    # some codes there


login = APPLogin()
