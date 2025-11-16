"""Simple JSON-backed memory bank for demo purposes."""
import json, os

class MemoryBank:
    def __init__(self, path='memory.json'):
        self.path = path
        if os.path.exists(self.path):
            with open(self.path,'r') as f:
                self.data = json.load(f)
        else:
            self.data = {'plans': [], 'prefs': {}}

    def save_plan(self, plan, grocery, prefs):
        entry = {'plan': plan, 'grocery': grocery, 'prefs': prefs}
        self.data['plans'].append(entry)
        self.data['prefs'].update({k:v for k,v in prefs.items() if k in ['diet','exclude']})
        with open(self.path,'w') as f:
            json.dump(self.data, f, indent=2)

    def get_recent(self, n=3):
        return self.data['plans'][-n:]
