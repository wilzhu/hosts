-----------------

**hosts for Internet Freedom & Block Game Websites

------------------

## Windows
用文本编辑器(如：Notepad++|记事本)打开`C:\Windows\System32\drivers\etc`中的hosts文件，
把 -> [hosts](https://raw.githubusercontent.com/gowiden/hosts/master/hosts) <- 全部内容复制到hosts文件中，保存后通过
```开始 -> 运行 -> 输入cmd -> 在CMD窗口输入ipconfig /flushdns```使其生效。
<br>**注意：如果遇到无法保存，请右键hosts->属性->安全，然后选择你登陆的用户名，最后点击编辑，勾选"写入"即可。**

## Linux
开启终端(快捷键为"Ctrl + Alt + T")输入`bash -c 'wget  https://raw.githubusercontent.com/gowiden/hosts/master/hosts -qO /tmp/hosts && sudo mv /tmp/hosts /etc/hosts'`
<br>最后在终端输入`sudo systemctl restart NetworkManager`
<br>**注意 : 非systemd发行版，终端输入`sudo rcnscd restart`，如果不清楚请两个都试一次**

## Mac OS
可以使用[Gas Mask](http://www.macupdate.com/app/mac/29949/gas-mask/)工具修改

或者在`/private/etc/`目录下新建或修改[hosts](https://raw.githubusercontent.com/gowiden/hosts/master/hosts)，然后终端输入`sudo killall -HUP mDNSResponder`使其生效。

## Android
请在`/system/etc`目录下新建或修改[hosts](https://raw.githubusercontent.com/gowiden/hosts/master/hosts)，然后通过`开启飞行模式 -> 关闭飞行模式 `的方式使其生效。

## iOS
请在`/etc`目录下新建或修改[hosts](https://raw.githubusercontent.com/gowiden/hosts/master/hosts)使其生效。

## Annoucement
* Linux、Mac、Android用户请用Notepad++ 转换文本编码和换行符格式，否则hosts可能会无法正常工作。参考[解决方案](http://www.zhihu.com/question/29064201/answer/63612656)。
* Android和iOS需要root权限和越狱后才能访问hosts文件。
* 由于部分App不支持[SNI](https://en.wikipedia.org/wiki/Server_Name_Indication)，故[不推荐在移动设备上使用](https://github.com/racaljk/hosts/wiki/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E6%8E%A8%E8%8D%90%E5%9C%A8%E7%A7%BB%E5%8A%A8%E8%AE%BE%E5%A4%87%E4%B8%8A%E4%BD%BF%E7%94%A8hosts%EF%BC%9F)
* 转载和使用过程中请保留hosts文件注释以及任何能体现版权的信息。
