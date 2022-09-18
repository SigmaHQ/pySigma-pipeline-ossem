import pytest
from sigma.pipelines.ossem import ossem_to_sigma
from sigma.rule import SigmaRule

def test_ossem_to_sigma():
    pipeline = ossem_to_sigma()
    rule = pipeline.apply(
        SigmaRule.from_yaml(f"""
            title: Test
            status: test
            logsource:
                category: process_creation
                product: windows
            detection:
                sel:
                    process_command_line: test
                    process_file_path: test
                    process_parent_command_line: test
                    process_parent_file_path: test
                condition: sel
        """)
    )
    fields = [
        detection_item.field
        for detection_item in rule.detection.detections["sel"].detection_items
    ]
    assert fields == [
        "CommandLine",
        "Image",
        "ParentCommandLine",
        "ParentImage",
    ]