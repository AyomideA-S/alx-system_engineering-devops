# Welcome to Shell Redirections...

## Description of each script
0. [`0-hello_world`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/0-hello_world)					: 	a script that prints "**Hello, World**", followed by a new line to the standard output
1. [`1-confused_smiley`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/1-confused_smiley)			: 	a script that displays a confused smiley `"(Ôo)'`
2. [`2-hellofile`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/2-hellofile)						:	a script that displays the content of the `/etc/passwd` file
3. [`3-twofiles`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/3-twofiles)						:	a script that displays the contents of `/etc/passwd` and `/etc/hosts`
4. [`4-lastlines`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/4-lastlines)						:	a script that displays the last **10** lines of `/etc/passwd`
5. [`5-firstlines`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/5-firstlines)					:	a script that displays the first **10** lines of `/etc/passwd`
6. [`6-third_line`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/6-third_line)					:	a script that displays the third line of the file `iacta`
7. [`7-file`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/7-file)								:	a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ended by a new line
8. [`8-cwd_state`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/8-cwd_state)						:	a script that writes into the file `ls_cwd_content` the result of the command `ls -la`
9. [`9-duplicate_last_line`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/9-duplicate_last_line)	:	a script that duplicates the last line of the file `iacta`
10. [`10-no_more_js`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/10-no_more_js)				:	a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders
11. [`11-directories`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/11-directories)				:	a script that counts the number of directories and sub-directories in the current directory, with the following requirements:
	* the current and parent directories should not be taken into account
	* hidden directories should be counted
12. [`12-newest_files`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/12-newest_files)			:	a script that displays the **10** newest files in the current directory, with the following requirements:
	* one file per line
	* sorted from the newest to the oldest
13. [`13-unique`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/13-unique)						:	a script that takes a list of words as input and prints only words that appear exactly once, with the following specifications:
	* Input format: One line, one word
	* Output format: One line, one word
	* words should be sorted
14. [`14-findthatword`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/14-findthatword)			:	a script that displays lines containing the pattern “**root**” from the file `/etc/passwd`
15. [`15-countthatword`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/15-countthatword)			:	a script that displays the number of lines that contain the pattern “**bin**” in the file `/etc/passwd`
16. [`16-whatsnext`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/16-whatsnext)					:	a script that displays lines containing the pattern “**root**” and **3** lines after them in the file `/etc/passwd`
17. [`17-hidethisword`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/17-hidethisword)			:	a script that displays all the lines in the file `/etc/passwd` that do not contain the pattern “**bin**”
18. [`18-letteronly`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/18-letteronly)				:	a script that display all lines of the file `/etc/ssh/sshd_config` starting with a letter
19. [`19-AZ`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/19-AZ)								:	a script that replaces all characters `A` and `c` from input to `Z` and `e` respectively
20. [`20-hiago`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/20-hiago)							:	a script that removes all letters `c` and `C` from input
21. [`21-reversed`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/21-reversed)					:	a script that reverses its input
22. [`22-users_and_homes`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/22-users_and_homes)		:	a script that displays all users and their home directories, sorted by users based on the `/etc/passwd` file

## Advanced tasks
23. [`100-empty_casks`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/100-empty_casks)			:	a script that finds all empty files and directories in the current directory and all sub-directories, with the following specifications:
	* only the names of the files and directories should be displayed (not the entire path)
	* hidden files should be listed
	* one file name per line
	* the listing should end with a new line
24. [`101-gifs`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/101-gifs)							:	a script that lists all the files with a `.gif` extension in the current directory and all its sub-directories, with the following specifications:
	* hidden files should be listed
	* Only regular files (not directories) should be listed
	* the names of the files should be displayed without their extensions
	* the files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`)
	* one file name per line
	* the listing should end with a new line
25. [`102-acrostic`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/102-acrostic)					:	a script that decodes acrostics that use the first letter of each line and ends with a new line
26. [`103-the_biggest_fan`](https://github.com/AyomideA-S/alx-system_engineering-devops/blob/master/0x02-shell_redirections/103-the_biggest_fan)	:	a script that parses web servers logs in _TSV_ format as input and displays the *11* hosts or IP addresses which did the most requests, with the following specifications:
	* order by number of requests, most active host or IP at the top
