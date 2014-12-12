Name: system-config-vsftpd
Version: 0.5.1
Release: 5%{?ns_dist}.15
Summary: A graphical interface for administering vsftpd server

Group: Applications/System
License: GPLv2+
URL: http://vsftpd-config.sf.net
Source0: http://downloads.sourceforge.net/vsftpd-config/%{name}-%{version}.tar.gz
Patch0: suresave.patch
Patch1: tra-zh_CN.patch
#Patch2: system-config-vsftpd-0.5.1-neolylin-bug21017.patch
Patch3: system-config-vsftpd-status_log-garbled.patch
Patch4: system-config-vsftpd-client.patch
Patch5: system-config-vsftpd-save1.patch
Patch6: system-config-vsftpd-0.5.1-neokylin-bug21017.patch
Patch7: system-config-vsftpd-0.5.1-neokylin-anonymous_log.patch
Patch8: system-config-vsftpd-0.5.1-neokylin-bug23180.patch
Patch9: system-config-vsftpd-0.5.1-neokylin-bug23487_bug23517.patch
Patch10: system-config-vsftpd-desktopname.patch
Patch11: system-config-vsftpd-bug20999.patch

#add by zhanghao
Patch12: system-config-vsftpd-0.5.1-neokylin-bug34802.patch
Patch13: system-config-vsftpd-0.5.1-neokylin-bug33367.patch
Patch14: system-config-vsftpd-0.5.1-neokylin-bug34879.patch
#done by zhanghao 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: desktop-file-utils, gettext, intltool, python
BuildArch: noarch
Requires: python >= 2.4, pygtk2, pygtk2-libglade, usermode, vsftpd

%description
System-config-vsftpd is a graphical utility for administrating 
Very Secure FTP Daemon ( VSFTPD ).

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install  DESTDIR=$RPM_BUILD_ROOT
make usermode DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor "fedora"  --delete-original         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

#%preun
#if [ $1 = 0 ]; then
#  if [ -d /usr/share/system-config-vsftpd ] ; then
#    rm -rf /usr/share/system-config-vsftpd/*.pyc
#  fi
#fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/%{name}
%{_sbindir}/%{name}

%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/pixmaps/system-config-vsftpd
%dir %{_datadir}/pixmaps/system-config-vsftpd/ico

%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/*.pyo

%{_datadir}/pixmaps/system-config-vsftpd.png
%{_datadir}/pixmaps/system-config-vsftpd/ico/*.png
%{_datadir}/kontrol-panel
%{_datadir}/applications
%{_datadir}/%{name}/system-config-vsftpd.glade

%attr(0644,root,root) %config(noreplace) /etc/security/console.apps/%{name}
%attr(0644,root,root) %config(noreplace) /etc/pam.d/%{name}

%changelog
* Mon Apr 14 2014 Zhang Hao <hao.zhang@cs2c.com.cn> - 0.5.1-5.ns6.15
- Patch12: resolve #34802: remove System from desktop file
- Patch13: resolve #34871 make option pasv_promiscuous correct
- Patch14: resolve #34879 remove print "aaa"

* Tue Aug 07 2012 CS2C Li Hanlin <hanlin.li@cs2c.com.cn> - 0.5.1-5.10
- Add delete_event and make the default path correct

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.5.1-4
- Added Requires: vsftpd (fix BZ#451369)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5.1-2
- Rebuild for Python 2.6

* Thu May 01 2008 Maros Barabas <mbarabas@redhat.com> - 0.5.1-1
- rebase from upstream

* Tue Oct 30 2007 Maros Barabas <mbarabas@redhat.com> - 0.4.5-3
- rebuild for rawhide

* Thu Oct 25 2007 Maros Barabas <mbarabas@redhat.com> - 0.4.5-2
-  fix problems with parsing file names with spaces in Transfer log

* Tue Aug 28 2007 Maros Barabas <mbarabas@redhat.com> - 0.4.5-1
- fix review bugs
- Resolve: #253858 (bugzilla.redhat.com)
- fix number of clients if passive com. used
- disable sensitive File->New and File->Open due to malfunction
- Add About dialog
- Add uninstall method to Makefile, few cosmetic changes in Makefile

* Wed Aug 22 2007 Maros Barabas <mbarabas@redhat.com> - 0.4.4-1
- Few changes in spec file because adding to Fedora-extras
- First steps of adding virtual users tab (still disabled
  in this version)
- Few cosmetic fixes

* Thu Aug 09 2007 Maros Barabas <mbarabas@redhat.com> - 0.4.3-2
- Added dialog for choosing a config file
- In transfer log on calendar day-change first possible IP
  is selected
- Changed version formating from X.x-y to X.x.y
- Removed warnings on gtk <2.10 in set_grid_lines function
- Added variable __LOCAL in main.py->__init__ for testing

* Wed Aug 08 2007 Maros Barabas <mbarabas@redhat.com> - 0.4-2
- Changed transfer log 

* Mon Jun 18 2007 Maros Barabas <mbarabas@redhat.com> - 0.3-1
- initializing
