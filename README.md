# Binwalk

![Build Status](https://github.com/OSPG/binwalk/actions/workflows/test.yml/badge.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/OSPG/binwalk/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/OSPG/binwalk.svg)](https://github.com/OSPG/binwalk/blob/master/LICENSE)

Binwalk is a fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images.

### EOL notice

This fork was born to fix some outsanding issues with binwalk v2 and generally to keep it in good shape. It served his purpose helping users and distro packagers alike. However, given the original author recently rewrote binwalk in rust and is in active development again, there is no need to maintain binwalk v2 anymore. Users and contributors should migrate to binwalk v3. This new version also provides a library in Rust, see https://github.com/ReFirmLabs/binwalk/wiki/Using-the-Rust-Library.

As a result, **this repository will effectively be EOL at 12/12/2025**, at which point this repository may be archived or removed.

-----

### Important notice

This is a fork of the original code from ReFirmLabs. This fork is maintained by the community and there is no relation between the maintainers of this fork and the original authors or the original company (though we greatly appreciate their work). 

If you want to contribute feel free to open issues, pull requests, or even ask to be added to the repository to help with reviewing and merging PR. 

### Alternative software

There seems to exist a well-maintained alternative called [unblob](https://unblob.org/). According to some reports it has better extraction capabilities (are able to extract more data and faster). The downside is that it doesn't detect as much filetypes as binwalk. Another important difference is the number of dependencies: while binwalk doesn't require any dependency (they are optional), unblob depends on almost 20 packages.

### *** Extraction Security Notice ***

Prior to Binwalk v2.3.3, extracted archives could create symlinks which point anywhere on the file system, potentially resulting in a directory traversal attack if subsequent extraction utilties blindly follow these symlinks. More generically, Binwalk makes use of many third-party extraction utilties which may have unpatched security issues; Binwalk v2.3.3 and later allows external extraction tools to be run as an unprivileged user using the `run-as` command line option (this requires Binwalk itself to be run with root privileges). Additionally, Binwalk v2.3.3 and later will refuse to perform extraction as root unless `--run-as=root` is specified.

### Installation and Usage

* [Installation](./INSTALL.md)
* [API](./API.md)
* [Supported Platforms](https://github.com/OSPG/binwalk/wiki/Supported-Platforms)
* [Getting Started](https://github.com/OSPG/binwalk/wiki/Quick-Start-Guide)
* [Binwalk Command Line Usage](https://github.com/OSPG/binwalk/wiki/Usage)
* [Binwalk IDA Plugin Usage](https://github.com/OSPG/binwalk/wiki/Creating-Custom-Plugins)

More information on [Wiki](https://github.com/OSPG/binwalk/wiki)
