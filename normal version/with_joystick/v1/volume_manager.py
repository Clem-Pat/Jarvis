from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class Volume_manager():
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    def manage_volume(self, command):
        if 'monte' in command : self.get_sound_up()
        elif 'baisse' in command : self.get_sound_down()
        elif 'tai' in command : self.volume.SetMasterVolumeLevel(-65.25, None) #set self to 0
        elif 'actuel' in command : print(int(self.convert_in_pourcent(self.volume.GetMasterVolumeLevel()))) #get the current sound
        else : self.set_sound(command)

    def convert_in_dB(self, num):
        if num <= 50: vol = -65.25 + 6.191*num - 0.463*num**2 + 21.425*(10**(-3))*(num**3) - 590.522*(10**(-6))*(num**4) + 9.751*(10**(-6))*(num**5) - 94.608*(10**(-9))*(num**6) + 496.978*(10**(-12))*(num**7) - 1.09*(10**(-12))*(num**8)
        else: vol = -26.18 + 0.381*num - 1.193*(10**(-3))*(num**2)
        return vol

    def convert_in_pourcent(self, vol):
        if vol >= -30: num = 99.815 + 6.268*vol + 0.115*(vol**2) - 3.087*(10**(-3))*(vol**3) - 163.966*(10**(-6))*(vol**4) - 2.251*(10**(-6))*(vol**5) - 9.415*(10**(-9))*(vol**6)
        else: num = 58.573 + 2.047*vol + 17.615*(10**(-3))*(vol**2)
        return num

    def set_sound(self, command="Volume : 11%"):
        if any(i.isdigit() for i in command):
            num = int(''.join([i for i in list(command) if i.isdigit()]))
            print(num)
            p=self.convert_in_dB(num)
            self.volume.SetMasterVolumeLevel(p, None)

    def get_sound_up(self):
        current_volume = self.convert_in_pourcent(self.volume.GetMasterVolumeLevel())
        volume_wanted = self.convert_in_dB(current_volume+10)
        if volume_wanted < 0:
            self.volume.SetMasterVolumeLevel(volume_wanted, None)
        else:
            self.volume.SetMasterVolumeLevel(0, None)
            print('Volume at 100%')

    def get_sound_down(self):
        current_volume = self.convert_in_pourcent(self.volume.GetMasterVolumeLevel())
        volume_wanted = self.convert_in_dB(current_volume-10)
        if volume_wanted > -65.25:
            self.volume.SetMasterVolumeLevel(volume_wanted, None)
        else:
            self.volume.SetMasterVolumeLevel(-65.25, None)
            print('Volume at 0')
