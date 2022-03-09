class WebSeedResponse:
     def __init__(self, seed_value, patchBytes, spoilerLogBytes = None) -> None:
        self.seed_value = seed_value
        self.patchBytes = patchBytes
        self.spoilerLogBytes = spoilerLogBytes