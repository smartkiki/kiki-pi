import soundcloud
import time
import vlc
import os

client = soundcloud.Client(client_id='57aef033f6f6477a54dfc34514cf4b1b')

def execute_intent(entities):
	for e in entities:
		if e.name == 'music':
			song = e.raw
			break

	track = client.get('/tracks', q=song)
	stream_url = client.get(track[0].stream_url, allow_redirects=False)
	os.system('say -v Daniel "Now Playing %s"' % song)
	_play_song_from_stream_url(stream_url.location)
	return "thanks for listening to %s. For playing more tunes just holler!" % song


def _play_song_from_stream_url(location):
	instance = vlc.Instance()
	p = instance.media_player_new()
	media = instance.media_new(location)
	p.set_media(media)
	p.play()
	timeout = time.time() + 45
	while True:
		if time.time() > timeout:
			p.stop()
			break
	return
