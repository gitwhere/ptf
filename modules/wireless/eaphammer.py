#!/usr/bin/env python
#####################################
# Installation module for EAPHammer
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Corey Batiuk (Skapunker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update EAPHammer - a toolkit for targeted evil twin attacks."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/s0lst1c3/eaphammer"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="eaphammer"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip,apache2,dnsmasq,libssl-dev,libnfnetlink-dev,libnl-3-dev,libnl-genl-3-dev,libcurl4-openssl-dev,zlib1g-dev,libpcap-dev,dsniff"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python -m pip install -r pip.req,cd hostapd-eaphammer/hostapd,make hostapd-eaphammer_lib"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="eaphammer"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""

