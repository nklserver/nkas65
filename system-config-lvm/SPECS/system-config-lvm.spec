# -*- RPM-SPEC -*-
Summary: A utility for graphically configuring Logical Volumes
Name: system-config-lvm
Version: 1.1.12
Release: 16%{?dist}%{?ns_dist}.03
URL: http://git.fedorahosted.org/git/?p=system-config-lvm.git 
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Applications/System
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: usermode-gtk, /sbin/chkconfig
Requires: gnome-python2, pygtk2, pygtk2-libglade, gnome-python2-canvas 
Requires: gnome-python2-bonobo, gnome-python2-gnome
Requires: urw-fonts
Requires: lvm2 >= 2.00.20
Requires: python >= 2.3
BuildRequires: perl(XML::Parser) gettext intltool
BuildRequires: desktop-file-utils

Patch0: scl-adjustement.patch
Patch1: scl-correct_localization.patch
Patch2: scl-duplicate_entry_fstab.patch
Patch3: scl-localization_update.patch
Patch4: scl-volume_change_fails.patch
Patch5: scl-volume_change_fails2.patch
Patch6: scl-unable_to_add_new_entry_to_fstab.patch
Patch7: scl-initialization-fails-with-EFI-GPT.patch
Patch8: scl-leaves-mount-for-lv.patch
Patch9: scl-logical_volumes_displayed_under_uninitialized.patch
Patch10: scl-get_partitions_valueerror.patch
Patch11: scl-logical_volumes_displayed_under_uninitialized-2.patch
Patch12: scl-traceback-parsing-dm.patch
Patch13: scl-extent.patch
Patch14: scl-1-many_lv.patch
Patch16: scl-raid1.patch
Patch17: scl-3-many_lv.patch
Patch18: scl-4-many_lv.patch
Patch19: scl-raid1-errormsg.patch
Patch20: scl-crash_with_striped_segments.patch
#neokylin add begin
Patch50: system-config-lvm-1.1.12-neokylin-bug34788.patch
Patch51: system-config-lvm-1.1.12-neokylin-bug34786.patch
Patch52: system-config-lvm-1.1.12-neokylin-bug35384.patch
#neokylin end

%description
system-config-lvm is a utility for graphically configuring Logical Volumes

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
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
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%patch50 -p1
%patch51 -p1
%patch52 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --vendor system --delete-original		\
  --dir %{buildroot}%{_datadir}/applications			\
  --remove-category Application					\
 --remove-category SystemSetup					\
  --remove-category X-Red-Hat-Base				\
  --add-category Settings					\
  --add-category System						\
  %{buildroot}%{_datadir}/applications/system-config-lvm.desktop

%find_lang %name

%clean
rm -rf %{buildroot}

#Replace the files line with the one commented out when translations are done
%files -f %{name}.lang
#%files

%defattr(-,root,root)
%doc COPYING
#%doc docs/ReleaseNotes
#%doc docs/html/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/applications/system-config-lvm.desktop
%{_datadir}/system-config-lvm
%config(noreplace) %{_sysconfdir}/pam.d/system-config-lvm
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-lvm

%changelog
* Wed May 21 2014 Zhang Hao <hao.zhang@cs2c.com.cn> - 1.1.12-16.ns6.03
- Patch52: resolve#bz35384 change xfs error

* Thu May 15 2014 Zhang Hao < hao.zhang@cs2c.com.cn> - 1.1.12-16.ns6.02
- Patch51: Resolves nkbz#34786 can't reload new lv filesytem

* Fri Mar 28 2014 Zhang Hao <hao.zhang@cs2c.com.cn> - 1.1.12-16.ns6.01
- Patch50:Resolves nkbz#34788

* Mon Jul 01 2013 Marek Grac <mgrac@redhat.com> - 1.1.12-16
- s-c-lvm crashes with striped segments in a mirror
  Resolves: rhbz#923643

* Thu Dec 13 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-15
- s-c-lvm improve error message when using mirrored LVM
  Resolves: rhbz#820539

* Mon Dec 10 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-14
- s-c-lv crash after startup on machine with many LV
  Resolves: rhbz#840070
- s-c-lvm crash when encounter RAID1 created in LVM
  Resolves: rhbz#852864

* Thu Sep 27 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-13
- s-c-lvm crash after startup on machine with many LV
- Resolves: rhbz#840070
- s-c-lvm crash when encounter RAID 1 created in LVM
- Resolves: rhbz#852864
- s-c-lvm crash on mirrored LV with mirrorlog
- Resolves: rhbz#852864

* Wed May 02 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-12
- Displays Logical Volumes without filesystem under 'Unitialized'
- Resolves: rhbz#791153
- s-c-lvm traceback on parsing "dmsetup ls" output 
- Resolves: rhbz#815921

* Mon Mar 19 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-11
- Crash on partitions named /dev/*p[0-9]
- Resolves: rhbz#726830

* Sat Feb 18 2012 Marek Grac <mgrac@redhat.com> - 1.1.12-10
- Displays Logical Volumes under 'Uninitialized' Physical Volumes
- Resolves: rhbz#791153

* Fri Aug 12 2011 Marek Grac <mgrac@redhat.com> - 1.1.12-9
- Leaves mount for logical group in fstab after it was removed
- Resolves: rhbz#722895

* Mon Jul 04 2011 Marek Grac <mgrac@redhat.com> - 1.1.12-8
- Unable to initialize partition with EFI GPT table
- Resolves: rhbz#708029

* Wed Jul 28 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-7
- Unable to add new entry to /etc/fstab 
- Resolves: rhbz#619040

* Fri Jun 18 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-6
- system-config-lvm spec file cleanups
- Modification of volume size fails
- Resolves: rhbz#604174 rhbz#603770

* Fri May 07 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-5
- Modification of volume size fails
- Update localization for supported languages
- Resolves: rhbz#585845 rhbz#584985

* Wed May 05 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-4
- Localization problem at startup
- Extending LV creates a duplicate entry in /etc/fstab
- Cannot start due to missing module gnome 
- Resolves: rhbz#579055 rhbz#586554 rhbz#585501

* Wed Feb 24 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-3
- Remove dependency on rhpl as it is not used anymore
- Resolves: rhbz#557593

* Mon Feb 15 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-2
- Deprecation warning when run from terminal
- Resolves: rhbz#565489 

* Fri Jan 22 2010 Marek Grac <mgrac@redhat.com> - 1.1.12-1
- New version from Fedora 12

* Wed Jan 13 2010 Marek Grac <mgrac@redhat.com> - 1.1.11-1
- New version from Fedora 12
