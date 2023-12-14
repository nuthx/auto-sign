# auto-sign

自用签到工具，支持常去的论坛获取积分和明日方舟森空岛

## Website

- Chiphell（签到）
- 4K 世界（签到）
- 天雪（模拟下载字幕）
- 花火学园（签到）
- 天使动漫（打工+签到）
- 明日方舟 森空岛（支持多账号）

## Usage

首次运行 `python main.py`，程序会在 `config` 下自动生成 `config.ini`，根据对应内容填写

可在 `main.py` 内修改每日签到时间，支持在指定时间至后面 8 分钟内随机运行

运行 `streamlit run webui.py` 可查看签到统计信息

## Docker

##### 路径映射：

`/app/config` ==> `/config`

`/app/data` ==> `/data`

`/app/log` ==> `/log`

##### 端口映射：

`8501` ==> `8501`
