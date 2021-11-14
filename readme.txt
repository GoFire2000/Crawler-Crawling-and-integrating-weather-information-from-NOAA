执行方法：python task.py
注释了：
1、从noaa网站爬取内容
2、将下载到目录中的压缩包解压并提出相应表格内容

注释内容在新环境跑的时候需要去掉注释重新执行一下，注意根据自己环境的解压软件和路径要修改命令，比如我的解压用7z，下载路径是download


ghcnd-stations是noaa的文档，保存站点和编号的对应关系


climateData.csv是最终整合的数据，记录了编号，城市名称，所属省份，TMAX，TMIN，PCRP，TAVG

其余csv是爬下来的数据