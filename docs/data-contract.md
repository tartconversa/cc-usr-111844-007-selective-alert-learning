# 资料交换约定

资料为 UTF-8 JSON，根对象包含 name、tables 和 options。tables 的每张表都必须出现，允许空表；记录中的约定字段必须存在，显式 null 保留来源未知的含义，不能与字段缺失混淆。额外字段及 options 可承载研究方案。金额和时间的具体口径如下。

| 表 | 字段 |
| --- | --- |
| alerts | alert, household, day, score, device, group, policy, selected, probability, urgent |
| labels | label_id, alert, observed_at, label, supersedes |
| policies | policy, start, end |
| capacity | day, slots |

label 是 0/1/null；label_id 是稳定标签记录标识，observed_at 是结果对运营方可知的日期，supersedes 指向前一标签记录的 label_id。probability 为实际执行策略下的已知边际选择概率，非异常风险。urgent 必选但仍占核实名额；冻结时点以后可知的标签不得进入该时点分析。

紧急单超过当日全部容量时必须显式呈现不可执行冲突，不能丢掉人工标记。某个 alert 的标签修订须同属该 alert，分叉或悬空 supersedes 不能静默选择一条。用于分析的 cutoff 与选择策略生效日属于独立输入，选择记录需能区分已知资料与后来补报。

analysis_core/alerts.py 中的公开函数用于原始核对。score_slice 保留当前参数及返回语义。原始资料查询不代表已经完成统计识别或政策判断。examples/study.json 是可读的合成资料，数值不表示真实地区或人群。

Archive 用 name 和完整内容摘要区分原始资料修订。相同内容重复存入不会增加修订，不同内容不会覆盖旧资料；read 以精确摘要读取。Study.tables 和 Study.options 每次返回独立副本。group_rows 用属性是否存在与属性值共同分组；numeric_summary 分别报告条数、有效数值及空值。已有资料结构、原始查询及归档读取继续对外可用。
