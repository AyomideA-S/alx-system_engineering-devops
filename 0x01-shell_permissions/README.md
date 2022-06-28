## Now we're dealing with permissions in the Linux operating system...

### Description of each script
0. [`0-iam_betty`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/0-iam_betty) 									: 	a script that switches the current user to the user `betty`
1. [`1-who_am_i`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/1-who_am_i)									:	a script that prints the effective username of the current user
2. [`2-groups`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/2-groups) 										:	a script that prints all the groups the current user is part of
3. [`3-new_owner`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/3-new_owner) 									:	a script that changes the owner of the file `hello` to the user `betty`
4. [`4-empty`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/4-empty) 											:	a script that creates an empty file called `hello`
5. [`5-execute`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/5-execute) 										:	a script that adds execute permission to the owner of the file `hello`
6. [`6-multiple_permissions`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/6-multiple_permissions) 			:	a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`
7. [`7-everybody`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/7-everybody)									:	a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
8. [`8-James_Bond`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/8-James_Bond)								:	a script that sets the permission to the file `hello` as follows:
	* Owner: no permission at all
	* Group: no permission at all
	* Other users: all the permissions
9. [`9-John_Doe`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/9-John_Doe)									:	a script that sets the mode of the file `hello` to this:
	```bash
	-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
	```
10. [`10-mirror_permissions`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/10-mirror_permissions)				:	a script that sets the mode of the file `hello` the same as `olleh`’s mode
11. [`11-directories_permissions`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/11-directories_permissions)	:	a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users without changing regular files
12. [`12-directory_permissions`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/12-directory_permissions)		:	a script that creates a directory called `my_dir` with permissions *751* in the working directory
13. [`13-change_group`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/13-change_group)							:	a script that changes the group owner to `school` for the file `hello`

### Advanced tasks
14. [`100-change_owner_and_group`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/100-change_owner_and_group)		:	a script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory
15. [`101-symbolic_link_permissions`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/101-symbolic_link_permissions)	:	a script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively
16. [`102-if_only`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/102-if_only)										:	a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`
17. [`103-Star_Wars`](https://github.com/AyomideA-S/alx-system_engineering-devops/tree/master/0x01-shell_permissions/103-Star_Wars) 								:	a script that will play the **Star Wars IV** episode in the terminal

NOTE: For the last script you might need to run
```bash
sudo apt install telnet
```
