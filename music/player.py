# import vlc

# player = vlc.MediaPlayer("/root/Desktop/Jarvis/music/Na Ja .mp3")

# player.play()

# import vlc
# Instance = vlc.Instance()
# player = Instance.media_player_new()
# #Media = Instance.media_new('http://localhost/postcard/GWPE.avi')
# Media = Instance.media_new_path('/root/Desktop/Jarvis/music/Na Ja .mp3')
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# import os

# os.system('/root/Desktop/Jarvis/music/NaJa.mp3')

from playsound import playsound
playsound('/root/Desktop/Jarvis/music/NaJa.mp3')
