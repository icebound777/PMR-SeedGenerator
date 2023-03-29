class WebSeedResponse:
     def __init__(self, seed_value, hash_items, patch_bytes, spoiler_log_bytes, palette_offset, cosmetics_offset, audio_offset, music_offset) -> None:
        self.seed_value = seed_value
        self.hash_items = hash_items
        self.patchBytes = patch_bytes
        self.spoilerLogBytes = spoiler_log_bytes
        self.palette_offset = palette_offset
        self.cosmetics_offset = cosmetics_offset
        self.audio_offset = audio_offset
        self.music_offset = music_offset