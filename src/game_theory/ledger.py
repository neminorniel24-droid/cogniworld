import json
from pathlib import Path
class GameTheoryLedger:
 def __init__(self,path=None): self.path=Path(path) if path else None;self.events=[]
 def record(self,a,step):
  for i in a.alive.nonzero(as_tuple=True)[0].tolist(): self.events.append({"step":int(step),"agent":int(i),"action":int(a.last_action[i]),"reward":float(a.last_reward[i]),"energy":float(a.energy[i]),"reputation":float(a.reputation[i]),"cooperation":float(a.cooperation[i]),"competition":float(a.competition_score[i]),"defection":float(a.defection_score[i]),"attack_success":float(a.attack_success[i]),"defection":float(a.defection[i]),"cooperation":float(a.cooperation[i]),"reputation":float(a.reputation[i]),"trust":float(a.trust[i]),"payoff":float(a.payoff[i]),"strategy_action":int(a.last_strategy_action[i])})
 def flush(self):
  if not self.path or not self.events:return
  self.path.parent.mkdir(parents=True,exist_ok=True)
  with self.path.open("a") as f:
   for e in self.events:f.write(json.dumps(e,sort_keys=True)+"\n")
  self.events.clear()
