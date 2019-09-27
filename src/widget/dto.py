from dataclasses import dataclass, field
import typing
import uuid

@dataclass(order=True)
class WidgetDto(object):
    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4, init=False)
    name: str = field(compare=False)
    weight_kg: float = field(compare=True)

    def values(self):
        return [
          str(self.id),
          self.name,
          self.weight_kg
        ]
