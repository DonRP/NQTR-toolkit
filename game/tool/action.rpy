init -5 python:
    class Act(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action """

        def __init__(self,
                    rooms: Optional[list[str]] = None,
                    tm_start: int = 0,
                    tm_stop: int = 25,
                    day_start: int = -1,
                    day_deadline: int = -1):

            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            self.rooms = self.rooms = rooms if rooms else []
            if self.day_start < 0:
                renpy.log("Warn: You have set day_start < 0, so it will be ignored")
            if self.day_deadline < 0:
                renpy.log(
                    "Warn: You have set day_deadline < 0, so it will be ignored")


    def getActions(actions: dict[str, Act], room: Room,  tm: TimeHandler):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts: list[Act] = []
        for act_id, act in actions.items():
            if room.id in act.rooms:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
            elif act_id in room.action_ids:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
        return acts


    def clearExpiredActions(actions: dict[str, Act], cur_day: int):
        """Delete Expired Actions"""
        actions_to_del = []
        for id, act in actions.items():
            if (act.day_deadline and act.day_deadline <= cur_day):
                actions_to_del.append(id)
        for act_id in actions_to_del:
            del actions[act_id]
        del actions_to_del
        return actions
