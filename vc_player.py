"""Advanced VC player stub: manage queue, simulate playing, hooks for real VC libs"""
import asyncio

class VCPlayer:
    def __init__(self):
        self.queue = []
        self.playing = False

    def enqueue(self, track: dict):
        self.queue.append(track)

    def get_queue(self):
        return list(self.queue)

    async def play_loop(self):
        self.playing = True
        while self.queue:
            track = self.queue.pop(0)
            print('Now playing (stub):', track)
            # simulate duration
            await asyncio.sleep(track.get('duration', 3))
        self.playing = False

vc_player = VCPlayer()
