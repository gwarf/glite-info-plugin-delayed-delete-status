# glite-info-plugin-delayed-delete-status

This component is used with Top BDII and is intented to updates GLUE state
attributes of delayed delete entries.
BDII documentation is available at
[gridinfo documentation site](https://gridinfo-documentation.readthedocs.io/).

## Installing from packages

### On RHEL-based systems

On RHEL-based systems, it's possible to install packages from [EGI UMD
packages](https://go.egi.eu/umd). The packages are build from this repository,
and tested to work with other components part of the Unified Middleware
Distritbution.

## Building packages

A Makefile allowing to build source tarball and packages is provided.

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
git clone https://github.com/EGI-Foundation/glite-info-plugin-delayed-delete-status.git
cd glite-info-plugin-delayed-delete-status
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
cd /source
yum install -y rpm-build yum-utils
yum-builddep -y glite-info-plugin-delayed-delete-status.spec
make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Installing from source

This procedure is not recommended for production deployment, please consider
using packages.

Get the source by cloning this repo and do a `make install`.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `glite-info-plugin-delayed-delete-status.spec`
  - Updating authors in `AUTHORS.md`
- Once the PR has been merged tag and release a new version in GitHub
  - Packages will be built using Travis and attached to the release page

## History

This work started under the EGEE project, and was hosted and maintained for a
long time by CERN. This is now hosted here on GitHub, maintained by the BDII
community with support of members of the EGI Federation.
