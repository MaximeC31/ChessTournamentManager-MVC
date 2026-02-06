import json
import os
from typing import Any


class BaseManager:

    def __init__(self, file_path: str, model_class: Any) -> None:
        self.file_path = file_path
        self.model_class = model_class
        self.data = self._load_data()

    def save(self, instance: Any) -> None:
        if instance not in self.data:
            self.data.append(instance)
        self._save_all()

    def _save_all(self) -> None:
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump([instance.to_dict() for instance in self.data], f, indent=4)

    def _load_data(self) -> list[Any]:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            data_list = json.load(f)
            return [self.model_class.from_dict(data) for data in data_list]

    def get_all(self) -> list[Any]:
        return self.data

    def delete(self, instance: Any) -> None:
        if instance in self.data:
            self.data.remove(instance)
            self._save_all()
