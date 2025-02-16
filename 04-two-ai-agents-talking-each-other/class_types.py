from dataclasses import dataclass

@dataclass
class Message:
    content: str

@dataclass
class AgentProfile:
    name: str
    personality: str
    mission: str