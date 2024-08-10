from sigma.pipelines.common import logsource_windows, windows_logsource_mapping
from sigma.processing.transformations import (
    AddConditionTransformation,
    FieldMappingTransformation,
    DetectionItemFailureTransformation,
    RuleFailureTransformation,
    SetStateTransformation,
)
from sigma.processing.conditions import (
    LogsourceCondition,
    IncludeFieldCondition,
    ExcludeFieldCondition,
    RuleProcessingItemAppliedCondition,
)
from sigma.processing.pipeline import ProcessingItem, ProcessingPipeline


def ossem_to_sigma() -> (
    ProcessingPipeline
):  # Processing pipelines should be defined as functions that return a ProcessingPipeline object.
    return ProcessingPipeline(
        name="OSSEM pipeline",
        priority=20,  # The priority defines the order pipelines are applied. See documentation for common values.
        items=[
            ProcessingItem(  # Field mappings
                identifier="ossem_field_mapping",
                transformation=FieldMappingTransformation(
                    {
                        "file_creation_time": "CreationUtcTime",
                        "file_path": "TargetFilename",
                        "file_previous_creation_time": "PreviousCreationUtcTime",
                        "module_is_signed": "Signed",
                        "module_path": "ImageLoaded",
                        "module_signature_status": "SignatureStatus",
                        "module_signature": "Signature",
                        "pipe_name": "PipeName",
                        "process_call_trace": "CallTrace",
                        "process_command_line": "CommandLine",
                        "process_company": "Company",
                        "process_current_directory": "CurrentDirectory",
                        "process_file_description": "Description",
                        "process_file_path": "Image",
                        "process_file_version": "FileVersion",
                        "process_granted_access": "GrantedAccess",
                        "process_guid": "ProcessGuid",
                        "process_id": "ProcessId",
                        "process_parent_command_line": "ParentCommandLine",
                        "process_parent_file_path": "ParentImage",
                        "user_agent_original": "userAgent",
                    }
                ),
            )
        ],
    )
