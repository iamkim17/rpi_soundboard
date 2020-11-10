import subprocess

class Sound():
    def __init__(self, model):
        self.model = model
        self.p = None

    def play(self, sound_number):
        if self.p is None:
            self.subprocess_init(sound_number)
        else:
            self.p.terminate()
            self.subprocess_init(sound_number)

    def subprocess_init(self, sound_number):
        self.p = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-volume", str(self.model.get_volume_for_sound(sound_number)*100), self.model.get_file_path_for_sound(sound_number)])

