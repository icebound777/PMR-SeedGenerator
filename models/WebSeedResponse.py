class WebSeedResponse:
     def __init__(self, seedID, patchBytes, spoilerLogBytes = None) -> None:
        self.seedID = seedID
        self.patchBytes = patchBytes
        self.spoilerLogBytes = spoilerLogBytes