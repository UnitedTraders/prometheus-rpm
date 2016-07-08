VERSION=0.12.0rc3
PWD=$(shell pwd)
EL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3}')
FULL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3 "." $$4}')
RPM_NAME=node-exporter-$(VERSION)-1.$(FULL_VERSION).x86_64.rpm
RPM_FILE=$(PWD)/rpmbuild/RPMS/x86_64/$(RPM_NAME)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/node_exporter/releases/download/$(VERSION)/node_exporter-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir -p "node_exporter-$(VERSION).linux-amd64" && tar xzvf *tar.gz -C "node_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/node_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz node_exporter-$(VERSION).linux-amd64.tar.gz node_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/node_exporter-$(EL_VERSION).spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/node-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

deploy-bintray: rpm
	curl -T $(RPM_FILE) -u$(CREDENTIALS) https://api.bintray.com/content/$(REPOSITORY)/node-exporter/$(VERSION)/$(RPM_NAME)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION).linux-amd64.tar.gz"
