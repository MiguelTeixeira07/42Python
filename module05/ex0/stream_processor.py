from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        result = f'Processed {len(data)} numeric values'
        result += f', sum={sum(data)}, avg={sum(data) / len(data)}'

        return result

    def validate(self, data: Any) -> bool:
        return data.__class__ is list[int]

    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f'Output: {result}'


def main() -> None:
    pass


if __name__ == '__main__':
    main()
