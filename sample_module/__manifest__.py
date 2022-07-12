{
    "version": "15.0.1.0.0",
    "name": "sample_module",
    "summary": "sample module to reproduce oca/oca-ci#33",
    "author": "Glo Networks",
    "website": "https://github.com/GlodoUK/oca-ci-issue-33",
    "depends": [
        "base_setup",
        "base_sparse_field",
        "connector",
        "component",
        "queue_job",
    ],
    "data": [],
    "license": "LGPL-3",
    "external_dependencies": {
        "bin": [],
        "python": ["pycurl"],
        "deb": ["libcurl4-openssl-dev"],
    },
}
