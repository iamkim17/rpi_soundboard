import subprocess

class Sound():
    def __init__(self, model):
        self.model = model

    def play(self, sound_number):
        #pygame.mixer.music.load(self.model.get_file_path_for_sound(sound_number))
        #pygame.mixer.music.set_volume(self.model.get_volume_for_sound(sound_number))
        subprocess.call(["ffplay", "-nodisp", "-autoexit", "-volume", "80", self.model.get_file_path_for_sound(sound_number)])
