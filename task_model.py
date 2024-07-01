from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Task:
    task_id: str
    command: str
    schedule: str
    dependencies: List[str] = field(default_factory=list)
    retries: int = 3
    retry_delay: int = 60  # in seconds
    timeout: Optional[int] = None  # in seconds
