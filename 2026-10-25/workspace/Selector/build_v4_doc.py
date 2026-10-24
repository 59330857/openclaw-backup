#!/usr/bin/env python3
"""Build Feishu v4.0 doc via API"""
import json, requests

DOC_ID = "Y4ysdhBDjouNO0xmejBcGaXGn7b"
TOKEN = "t-g1044mcoRMJVN7IVRN43TBBLD6TJU5YD73QHYG3X"
BASE = "https://open.feishu.cn/open-apis"

def add_blocks(children):
    url = f"{BASE}/docx/v1/documents/{DOC_ID}/blocks/{DOC_ID}/children"
    r = requests.post(url, headers={"Authorization": f"Bearer {TOKEN}"}, json={"children": children, "index": -1})
    if r.status_code != 200:
        print(f"ERROR: {r.text}")
    else:
        data = r.json()
        if data.get("code") != 0:
            print(f"API ERROR: {data.get('msg')}")
        else:
            print(f"  +{len(children)} blocks ok, rev={data['data']['document_revision_id']}")
    return r.json()

def t(text, bold=False):
    return {"text_run": {"content": text, "text_element_style": {"bold": bold}}}

def p(text, bold=False):
    return {"block_type": 2, "text": {"elements": [t(text, bold)], "style": {"align": 1, "folded": False}}}

def h1(text):
    return {"block_type": 3, "heading1": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

def h2(text):
    return {"block_type": 4, "heading2": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

def h3(text):
    return {"block_type": 5, "heading3": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

def divider():
    return {"block_type": 22, "divider": {}}

def quote(text):
    return {"block_type": 15, "quote": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

def ordered(text):
    return {"block_type": 13, "ordered": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

def bullet(text):
    return {"block_type": 12, "bullet": {"elements": [t(text)], "style": {"align": 1, "folded": False}}}

print("=== Building v4.0 document ===")

# Section 1: 精准流量词
add_blocks([h2("一、精准流量词 → TK精准标签词"), divider()])
add_blocks([h1("亚马逊逻辑"), p("精准词 = 能精准描述功能、材质、特征、场景、对象的词")])
add_blocks([h1("TikTok Shop 东南亚适配")])
add_blocks([p("流量词类型    亚马逊 → TikTok Shop", bold=True)])
add_blocks([p("核心词          搜索关键词 → Hashtag标签（越南语/泰语本地化）")])
add_blocks([p("长尾词          精准属性词 → 场景词 + 人群词 + 用途词")])
add_blocks([p("找竞品方式    关键词反查 → 达人视频标签反查")])
add_blocks([p(" ")])
add_blocks([p("精准标签词的作用（TK版本）：", bold=True), bullet("找到直接竞品 → 做市场/竞品分析"), bullet("广告架构简单 → TK内容种草+小店闭环，转化有保障"), bullet("反查流量成本 → 算短视频CPM/带货GMV投产比"), bullet("判断真蓝海：小众+有精准标签+弱竞品=真蓝海；小众+无精准标签=没市场")])
add_blocks([p("标签词获取方法：", bold=True), bullet("EchoTik商品搜索 → 看关联标签"), bullet("TikTok搜索 $关键词 + 带货 → 看达人视频标签"), bullet("越南语/泰语本地化精准词（必须本地语言！）")])

# Section 2: 短视频种草友好度
add_blocks([divider(), h2("二、评估新品短视频种草友好度（新品好不好起）"), divider()])
add_blocks([h1("亚马逊逻辑"), p("看新品（≤30评）前5销量 ÷ 头部前5销量 > 20%")])
add_blocks([h1("TikTok版本：看短视频冷启动能力")])
add_blocks([p("信号 → 含义", bold=True)])
add_blocks([p("0基础视频也能跑出量 → 市场需求旺，内容驱动有效")])
add_blocks([p("无粉丝账号发视频也能出单 → 对新手友好，流量分配去中心化")])
add_blocks([p("低评分也能卖 → 市场不饱和，评价体系尚未固化")])
add_blocks([p("FBM/Shipping也稳定出单 → 物流不是核心瓶颈")])
add_blocks([p(" ")])
add_blocks([p("TK核心冷启动指标：", bold=True), bullet("新品视频发出去48h内自然播放量"), bullet("0基础账号发视频的带货转化率"), bullet("同类视频平均GMV vs 新品GMV占比")])
add_blocks([p("判断标准：", bold=True)])
add_blocks([quote("新品短视频种草系数 = 新品48h播放量 / 同类平均播放量 > 30% = 对新品友好，市场机会大 < 15% = 新品难以起量，慎入")])

# Section 3: 投产比与资金效率
add_blocks([divider(), h2("三、投产比与资金效率"), divider()])
add_blocks([p("标准（与亚马逊一致）：投产比 ≥ 120%", bold=True)])
add_blocks([p("TK版投产比计算：", bold=True), bullet("短视频投产比 = (GMV - 成本) / 投放成本 × 100%"), bullet("自然流量投产比 = GMV / 运营成本 × 100%")])
add_blocks([p("看两点：", bold=True), bullet("市场健康度：大量竞品投产差 = 市场不健康"), bullet("资金效率：TK回款周期比亚马逊快，但高周转仍是关键")])
add_blocks([p("越南站利润模型（v3.0）：", bold=True)])
add_blocks([quote("售价_RMB = 售价_VND / 3570\n总平台成本 = 售价_RMB × 41% + 2（含达人）\n真实毛利润 = 售价_RMB - 进货价 - 物流费 - 总平台成本\n真实毛利率 = 真实毛利润 / 售价_RMB\n\n毛利率要求：单件 ≥ 20%，套装款 ≥ 40%")])
add_blocks([p("泰国站：", bold=True)])
add_blocks([quote("售价 (THB) = (1688采购价CNY + 头程运费CNY) × 5.0 × 1.25\n毛利率要求：≥ 25%")])

# Section 4: 差异化+供应链
add_blocks([divider(), h2("四、差异化 + 供应链匹配度"), divider()])
add_blocks([h1("亚马逊差异化方向")])
add_blocks([p("产品：改款、组合、变体；人群/场景/用途重新定义；视觉、文案、评论差异化")])
add_blocks([h1("TK发饰差异化方向（完全适用）")])
add_blocks([p("差异化维度 → 具体做法", bold=True)])
add_blocks([p("产品变体 → 颜色（5-10色）× 规格（S/M/L）× 套装")])
add_blocks([p("人群细分 → 儿童款 / 少女款 / 妈妈款 / 职场款")])
add_blocks([p("场景重新定义 → 日常款 → 派对款 / 婚礼款 / 度假款")])
add_blocks([p("视觉差异化 → 场景化种草视频（ vs 白底图）")])
add_blocks([p("套装组合 → 发夹+发圈套装、节日礼盒装")])
add_blocks([p("供应链要求（必须满足）：", bold=True), bullet("能找到厂"), bullet("工艺能做"), bullet("起订量能满足"), bullet("发货时效 ≤ 48h")])

# Section 5: 进场时间节点
add_blocks([divider(), h2("五、进场时间节点（旺季前置）—— 核心！"), divider()])
add_blocks([h1("亚马逊原则"), p("旺季前1-2个月入场，选品看未来3-5个月是旺季的品")])
add_blocks([h1("TK版本（更激进！）")])
add_blocks([p("节日 → 日期 → TK布局时间 → 提前量", bold=True)])
add_blocks([p("母亲节 → 5月第2个周日 → 3月中-4月中 → 45-60天")])
add_blocks([p("国庆节（越南）→ 9月2日 → 7月 → 60天")])
add_blocks([p("圣诞节 → 12月25日 → 10-11月 → 60-90天")])
add_blocks([p("春节 → 1-2月 → 11-12月 → 60-90天")])
add_blocks([p("情人节 → 2月14日 → 1月 → 30-45天")])
add_blocks([p(" ")])
add_blocks([p("关键差异：", bold=True)])
add_blocks([p("亚马逊：旺季前1-2个月开始爆 → 旺季前1-2个月入场")])
add_blocks([p("TikTok：可能提前1个月才爆，爆发更快更猛 → 调研要更早，动作要更快")])
add_blocks([p("目的（与亚马逊一致）：", bold=True), bullet("提前攒评论"), bullet("提前养链接权重"), bullet("提前积累达人资源"), bullet("接住流量高峰")])

# Section 6: 季节性/节日性
add_blocks([divider(), h2("六、季节性 / 节日性 / 活动产品"), divider()])
add_blocks([h1("核心原则（与亚马逊一致）")])
add_blocks([quote("节日/季节品必须提前4-5个月布局\n现在爆的品 = 已经来不及进\n精铺可以做，但必须前置调研 + 前置备货")])
add_blocks([h1("TK更强的原因")])
add_blocks([bullet("短视频传播速度 >> 搜索"), bullet("节日氛围内容容易病毒传播"), bullet("直播 + 短视频双驱动"), bullet("东南亚节日氛围浓厚（母亲节、情人节购买力强）")])
add_blocks([p("越南/泰国重点节日（完整版）：", bold=True)])
add_blocks([p("春节 → 1-2月 → 红色系、礼盒装 → 节前60-90天")])
add_blocks([p("情人节 → 2月14日 → 粉色系、情侣款、心形款 → 节前45天")])
add_blocks([p("妇女节 → 3月8日 → 优雅款、花朵款 → 节前30天")])
add_blocks([p("母亲节 → 5月第2周日 → 礼盒装、感恩款 → 节前45-60天")])
add_blocks([p("国庆节（越南）→ 9月2日 → 越南元素、国旗色 → 节前30天")])
add_blocks([p("圣诞节 → 12月25日 → 金红色、节日限定、礼盒 → 节前60-90天")])

# Section 7: 合规与侵权风险
add_blocks([divider(), h2("七、合规与侵权风险（保命项）—— 更严！"), divider()])
add_blocks([h1("亚马逊三大风险")])
add_blocks([bullet("外观专利、发明专利"), bullet("版权侵权（TRO重灾区）：书籍、画作、影视IP、人物、图片等"), bullet("平台政策合规")])
add_blocks([h1("TK东南亚版本（更严格！）")])
add_blocks([p("风险类型 → 亚马逊 vs TikTok Shop", bold=True)])
add_blocks([p("IP侵权 → 高压线 → 生命线！爆款视频+商品一起下架")])
add_blocks([p("外观专利 → 必须排查（越南/泰国均有本地专利）")])
add_blocks([p("版权侵权 → TRO风险 → 内容会被截图举报，传播更快")])
add_blocks([p("材质合规 → 重要 → 更重要（镍释放量、邻苯二甲酸盐等）")])
add_blocks([p(" ")])
add_blocks([p("IP侵权黑名单（发饰高压线）：", bold=True), bullet("Disney：米奇、冰雪奇缘、公主系列"), bullet("Sanrio：Hello Kitty、美乐蒂、库洛米"), bullet("Line Friends：布朗熊、莎莉鸡"), bullet("动漫IP：火影、海贼王、鬼灭之刃"), bullet("奢侈品：Dior、Chanel、Gucci（logo/经典元素）")])
add_blocks([p("平台禁售/限售：", bold=True), bullet("政治/宗教内容"), bullet("虚假宣传"), bullet("材质不合规（镍释放超标、邻苯二甲酸盐超标）"), bullet("儿童用品安全问题（发饰针对儿童需额外认证）")])

# Section 8: 变体循环布局
add_blocks([divider(), h2("八、发货数量 + 变体循环布局"), divider()])
add_blocks([h1("亚马逊逻辑"), p("首批备货：参考≤30评竞品平均销量的50%；变体布局：引流→销售→备用→补货；分散库存防差评影响")])
add_blocks([h1("TK发饰版本（变体堆叠是杀手锏！）")])
add_blocks([p("变体维度 → 可扩展数量 → 效果", bold=True)])
add_blocks([p("颜色变体 → 5-10 色 → 评论共享，5个颜色=1个链接")])
add_blocks([p("规格变体 → 3+ 种 → S/M/L 多规格覆盖")])
add_blocks([p("套装形式 → 2+ 种 → 2件套/5件套/节日礼盒")])
add_blocks([p(" ")])
add_blocks([p("变体堆叠落地策略：", bold=True)])
add_blocks([quote("一次性上架所有颜色变体 → 评论全部累计共享\n↓\n5个颜色只有1个链接 → 评价积累速度 x5\n↓\n搜索权重集中 → 自然流量集中\n↓\n降低广告依赖 → 利润率提升")])
add_blocks([p("首批备货计算：", bold=True)])
add_blocks([quote("首批备货量 = EchoTik热销款月销量 × 20-30%\n结合历史波动调整，避免积压/断货")])
add_blocks([p("变体布局时序：", bold=True), bullet("测试变体：先上3-5个颜色测试"), bullet("爆量变体加码：哪颜色出单快，快速补充库存"), bullet("滞销变体淘汰：2周无动销则下架"), bullet("节日变体前置：节日前45天准备好特殊颜色/包装")])

print("\n=== Basic sections done, adding scoring system ===")

# Section 9: 综合评分系统
add_blocks([divider(), h2("九、综合评分系统（满分170分）"), divider()])
add_blocks([h1("评分矩阵")])
add_blocks([p("维度 → 分值 → 通过标准", bold=True)])
add_blocks([p("市场需求 → 25 → TikTok/Shopee/Google Trends 至少2项达标")])
add_blocks([p("竞争强度 → 25 → 卖家数<500 且市场集中度<40%")])
add_blocks([p("利润空间 → 25 → 真实毛利率≥30%（套装款按套装毛利率）")])
add_blocks([p("供应链稳定 → 15 → 供应商评分≥4.5，回头率≥15%")])
add_blocks([p("合规风险 → 15 → 无认证要求或易获取，无侵权")])
add_blocks([p("短视频种草友好度 ⭐ → 25 → 新品48h播放量/同类均值>30%")])
add_blocks([p("变体扩展潜力 ⭐ → 25 → 颜色≥5 或规格≥3 或套装≥2种")])
add_blocks([p("季节性/节日性 ⭐ → 25 → 季节匹配 or 节日关联 or 提前布局达标")])
add_blocks([p("套装化可行性 ⭐ → 28 → 套装组合合理+礼盒属性+客单价提升≥2.5倍")])
add_blocks([p(" ")])
add_blocks([h1("决策阈值")])
add_blocks([p("≥130分 → ⭐⭐⭐⭐⭐ S级（强烈推荐）→ 立即采样，重点推广，变体+套装一起上")])
add_blocks([p("115-129分 → ⭐⭐⭐⭐ A级（正常上架）→ 正常上架流程")])
add_blocks([p("100-114分 → ⭐⭐⭐ B级（优化后上架）→ 优化后上架")])
add_blocks([p("<100分 → ⭐ 放弃（C级）→ 记录原因，不投入")])
add_blocks([p(" ")])
add_blocks([h1("否决项（直接放弃）")])
add_blocks([bullet("真实毛利率 < 20%"), bullet("供应商评分 < 4.0"), bullet("Google Trends 下降趋势 > 30%"), bullet("明确品牌侵权"), bullet("属性一致性差"), bullet("新品短视频种草系数 < 15%")])

# Section 10: 三轨道选品策略
add_blocks([divider(), h2("十、三轨道选品策略"), divider()])
add_blocks([h1("轨道 1：主动选品（数据分析驱动）"), p("数据源：TikTok Shop后台/泰国越南站点热搜榜、EchoTik行业数据"), p("筛选逻辑：增长率↑ + 竞争度↓ + 利润率↑ + 短视频种草系数↑")])
add_blocks([h1("轨道 2：跟品策略（爆款跟随）"), p("数据源：EchoTik热销榜、妙手/店小秘ERP采集、1688同款比对"), p("筛选逻辑：销量绝对值↑ + 毛利达标 + 搬运可行性")])
add_blocks([h1("轨道 3：1688直选（供应链驱动）"), p("数据源：1688商品搜索"), p("筛选逻辑：进货价¥3-15、一件代发、48h发货 → 交叉验证")])

# Section 11: 飞书多维表格
add_blocks([divider(), h2("十一、飞书多维表格配置"), divider()])
add_blocks([p("App Token：AKppbAeyXanToTsVl6ScxO5QnZd", bold=True)])
add_blocks([p("Table ID：tblHU2do30jzinJT", bold=True)])
add_blocks([p("视图配置：", bold=True), bullet("📊 全部商品：默认视图"), bullet("🏆 S级推荐：过滤等级=S级"), bullet("💰 高利润商品：过滤利润率≥50%"), bullet("📈 高增长商品：过滤增长率≥30%"), bullet("⚠️ 待审核：过滤采集状态=待审核")])

# Section 12: 工作节奏
add_blocks([divider(), h2("十二、工作节奏与行为准则"), divider()])
add_blocks([h1("工作节奏")])
add_blocks([p("9:00-9:45 → 数据采集→初筛→利润测算→等级判定→短视频种草评估（自动）")])
add_blocks([p("10:00 → 同步至飞书多维表格 + 推送通知（自动）")])
add_blocks([p("人工时段 → 审核推荐结果、确认采购、下单采集（人工）")])
add_blocks([p(" ")])
add_blocks([h1("行为准则")])
add_blocks([bullet('数据真实性：绝不伪造数据，暂时无法获取的指标标记为「暂无数据」'), bullet('IP零容忍：发现任何IP侵权风险商品，无论利润多高，一律排除'), bullet('利润优先：毛利率不达标（泰<25%/越<20%）的商品一律不推荐'), bullet('及时更新：差评率上升、竞争加剧时，主动下调等级或移出推荐池'), bullet('中文输出：所有报告、通知、摘要均使用中文'), bullet('短视频种草优先：优先选择对短视频内容友好的商品，内容驱动 > 搜索驱动')])

# Version history
add_blocks([divider(), h2("版本历史"), divider()])
add_blocks([p("v2.0 → 2026-03 → 基础选品框架，3轨道+3打法")])
add_blocks([p("v3.0 → 2026-04 → 利润模型更新（越南站41%+¥2），评分系统升级至170分")])
add_blocks([p("v4.0 → 2026-04-22 → 融合亚马逊精铺8大维度，新增短视频种草友好度评估，TK标签词体系，进场时间节点更激进")])

print("\n=== Document built successfully! ===")
print(f"Doc ID: {DOC_ID}")
print(f"URL: https://www.feishu.cn/docx/{DOC_ID}")
