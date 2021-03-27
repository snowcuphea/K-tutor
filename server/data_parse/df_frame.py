# 키워드
kw_columns = (
    "id",
    "content",
    "count"
    "meaning",
    "cpcq"
)

# cpcq: 구어체 말뭉치
cpcq_columns = (
    "id",
    "kor",
    "eng"
)

# cpct : 문화 말뭉치
cpct_columns = (
    "kor",
    "eng",
    "cs"
)

# cs : 문화 출처
cs_columns = (
    "type",
    "name"
)

# kw_in_cpcq: 각 cpcq가 포함하는 kw
kcq_columns = (
    "id",
    "kw_id",
    "cpcq_id"
)