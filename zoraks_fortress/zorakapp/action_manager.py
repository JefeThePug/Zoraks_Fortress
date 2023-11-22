class ActionManager:
    def __init__(self, **kwargs):
        self.action = kwargs["verb"]
        del kwargs["verb"]
        self.kwargs = kwargs

    def run_action(self) -> int:
        funcs = {
            "inventory": self.cmd_inventory,
            "inspect": self.cmd_inspect,
            "attack": self.cmd_attack,
            "close": self.cmd_close,
            "again": self.cmd_again,
            "open": self.cmd_open,
            "talk": self.cmd_talk,
            "look": self.cmd_look,
            "give": self.cmd_give,
            "take": self.cmd_take,
            "cast": self.cmd_cast,
            "undo": self.cmd_undo,
            "save": self.cmd_save,
            "load": self.cmd_load,
            "quit": self.cmd_quit,
            "put": self.cmd_put,
            "map": self.cmd_map,
            "go": self.cmd_go,
        }
        success = funcs[self.action](**self.kwargs)
        return success

    def cmd_go(self, **kwargs) -> int:
        print("go")

    def cmd_put(self, **kwargs) -> int:
        pass