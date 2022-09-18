![Tests](https://github.com/SigmaHQ/pySigma-pipeline-ossem/actions/workflows/test.yml/badge.svg)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/SigmaHQ/cc7404e671dcceed6492d12674f2f517/raw/SigmaHQ-pySigma-pipeline-ossem.json)
![Status](https://img.shields.io/badge/Status-pre--release-orange)

# pySigma OSSEM Pipeline

This is the OSSEM pipeline for pySigma. It contains the `ossem_to_sigma` processing pipeline in `sigma.pipelines.ossem`,
that transforms Sigma rules written with the field naming and value formats defined in the [OSSEM
project](https://ossemproject.com) into the default Sigma taxonomy. Example:

```
title: Rule written with the OSSEM taxonomy.
status: stable
taxonomy: ossem
logsource:
    category: process_creation
    product: windows
detection:
    sel:
        process_command_line: whoami
        process_file_name: whoami.exe
        process_parent_file_name: httpd.exe
    condition: sel
```

By preprocessing this rule with the *ossem_to_sigma* pipeline it can be used like any other Sigma rule written in the
default Sigma taxonomy.

This backend is currently maintained by:

* tbd