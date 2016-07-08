VERSION=0.6
PWD=$(shell pwd)
EL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3}')
FULL_VERSION=$(shell rpm -q --whatprovides /etc/redhat-release | awk -F'.' '{print $$3 "." $$4}')
RPM_NAME=jmx-exporter-$(VERSION)-1.$(FULL_VERSION).x86_64.rpm
RPM_FILE=$(PWD)/rpmbuild/RPMS/x86_64/$(RPM_NAME)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)/configuration"
	cd "$(PWD)/rpmbuild/SOURCES/" && wget https://github.com/prometheus/jmx_exporter/archive/parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/" && unzip -o parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && mvn clean package
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-$(VERSION)-jar-with-dependencies.jar ../jmx_exporter-$(VERSION)/jmx_exporter.jar
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp example_configs/* ../jmx_exporter-$(VERSION)/configuration
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz parent-$(VERSION).tar.gz jmx_exporter-$(VERSION)
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/jmx_exporter-$(EL_VERSION).spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=jmx_exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/jmx_exporter/rpmbuild/RPMS/x86_64/jmx_exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

deploy-bintray: rpm
	curl -T $(RPM_FILE) -u$(CREDENTIALS) https://api.bintray.com/content/$(REPOSITORY)/jmx-exporter/$(VERSION)/$(RPM_NAME)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/parent-$(VERSION).tar.gz"
