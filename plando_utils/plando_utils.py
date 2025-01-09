class TransformedPlandoData():
    def __init__(self, plando_data: dict | None) -> None:
        if plando_data is None:
            self.boss_battles: dict[int, int] | None = None
            self.required_spirits: list[int] | None = None
            self.difficulty: dict[int, int] | None = None
            self.move_costs: dict[str, dict[str, dict[str, int]]] | None = None
            return

        self.boss_battles: dict[int, int] | None  = plando_data.get("boss_battles")
        self.required_spirits: list[int] | None = plando_data.get("required_spirits")
        self.difficulty: dict[int, int] | None = plando_data.get("difficulty")
        self.move_costs: dict[str, dict[str, dict[str, int]]] | None = plando_data.get("move_costs")
