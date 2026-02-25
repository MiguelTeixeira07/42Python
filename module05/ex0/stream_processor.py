from typing import Any, List
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
        try:
            _ = data[0]
        except Exception:
            return False

        for item in data:
            try:
                _ = item + 0
            except Exception:
                return False

        return True


class TextProcessor(DataProcessor):
    keywords = ['ERROR',
                'INFO',
                'ALERT',
                'DEBUG']

    def process(self, data: Any) -> str:
        output = 'Processed text: '
        output += f'{len(data)} characters, {data.count(" ") + 1} words'

        return output

    def validate(self, data: Any) -> bool:
        try:
            _ = data[0]
        except Exception:
            return False

        for item in data:
            try:
                _ = item + ''
            except Exception:
                return False

        for keyword in self.keywords:
            if keyword in data:
                return False

        return True


class LogProcessor(DataProcessor):
    keywords = ['ERROR',
                'INFO',
                'ALERT',
                'DEBUG']

    def process(self, data: Any) -> str:
        output = ''

        for word in self.keywords:
            if word in data:
                match word:
                    case 'ERROR' | 'ALERT':
                        output = '[ALERT]'
                        offset = 6
                    case 'INFO':
                        output = '[INFO]'
                        offset = 5
                    case 'DEBUG':
                        output = '[DEBUG]'
                        offset = 6

                break

        output += f' {word} level detected: {data[offset:]}'

        return output

    def validate(self, data: Any) -> bool:
        try:
            _ = data[0]
        except Exception:
            return False

        for item in data:
            try:
                _ = item + ''
            except Exception:
                return False

        for keyword in self.keywords:
            if keyword in data:
                return True

        return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")
    numeric_processor: DataProcessor = NumericProcessor()
    numeric_data: List[int] = [1, 2, 3, 4, 5]

    try:
        print(f"Processing data: {numeric_data}")
        if numeric_processor.validate(numeric_data):
            print("Validation: Numeric data verified")
            result: str = numeric_processor.process(numeric_data)
            print(numeric_processor.format_output(result))
        else:
            print("Validation failed for numeric data.")
    except Exception as e:
        print(f"Error processing numeric data: {e}")

    print()
    print("Initializing Text Processor...")
    text_processor: DataProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"

    try:
        print(f'Processing data: "{text_data}"')
        if text_processor.validate(text_data):
            print("Validation: Text data verified")
            result = text_processor.process(text_data)
            print(text_processor.format_output(result))
        else:
            print("Validation failed for text data.")
    except Exception as e:
        print(f"Error processing text data: {e}")

    print()
    print("Initializing Log Processor...")
    log_processor: DataProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"

    try:
        print(f'Processing data: "{log_data}"')
        if log_processor.validate(log_data):
            print("Validation: Log entry verified")
            result = log_processor.process(log_data)
            print(log_processor.format_output(result))
        else:
            print("Validation failed for log data.")
    except Exception as e:
        print(f"Error processing log data: {e}")

    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    procs = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    test_d = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for index, (proc, data) in enumerate(zip(procs, test_d), start=1):
        try:
            if proc.validate(data):
                result = proc.process(data)
                print(f"Result {index}: {proc.format_output(result)}")
            else:
                print(f"Result {index}: Validation failed.")
        except Exception as e:
            print(f"Result {index}: Error - {e}")

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == '__main__':
    main()
