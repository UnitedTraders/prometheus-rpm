# prometheus-rpm
Stuff to build rpms for prometheus, node_exporter and alertmanager for amd64 until rpms are provided by the prometheus.io project itself.

Requires rpmbuild to be installed. To run, simply go into a subdir and run make. 

Use `make` to build for RHEL6 or RHEL7.

Use `make deploy-bintray` to build rpm and upload to bintray. Please set `CREDENTIALS` to `<user_name>:<API_KEY>`, `REPOSITORY` to `<user_name>/<repo_name>`.
