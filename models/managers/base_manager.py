import json
import os
from typing import Any


class BaseManager:

    def __init__(self, model_class: Any) -> None:
        self.model_class = model_class
        self.file_path = f"data/{self.model_class.__name__.lower()}s.json"
        self.data = self._load_data()

    def save(self, instance: Any) -> None:
        if instance not in self.data:
            self.data.append(instance)
        self._save_all()

    def _save_all(self) -> None:
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w") as file:
            json.dump([instance.to_dict() for instance in self.data], file, indent=4)

    def _load_data(self) -> list[Any]:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:
            data_list = json.load(file)
            return [self.model_class(**data) for data in data_list]

    def get_all(self) -> list[Any]:
        return self.data

    def delete(self, instance: Any) -> None:
        if instance in self.data:
            self.data.remove(instance)
            self._save_all()
