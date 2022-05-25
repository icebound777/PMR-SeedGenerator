class WebSeedResponse:
     def __init__(self, seed_value, patch_bytes, spoiler_log_bytes, palette_offset, cosmetics_offset) -> None:
        self.seed_value = seed_value
        self.patchBytes = patch_bytes
        self.spoilerLogBytes = spoiler_log_bytes
        self.palette_offset = palette_offset
        self.cosmetics_offset = cosmetics_offset