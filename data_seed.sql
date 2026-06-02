-- =====================================================
-- ENTITIES
-- =====================================================

INSERT INTO entities (
    id,
    name,
    ticker,
    aliases,
    created_at,
    updated_at
)
VALUES
(
    '11111111-1111-1111-1111-111111111111',
    'Hero MotoCorp',
    'HEROMOTOCO',
    ARRAY['Hero', 'Hero Motors'],
    NOW(),
    NOW()
),
(
    '22222222-2222-2222-2222-222222222222',
    'Reliance Industries',
    'RELIANCE',
    ARRAY['Reliance'],
    NOW(),
    NOW()
),
(
    '33333333-3333-3333-3333-333333333333',
    'Tata Consultancy Services',
    'TCS',
    ARRAY['TCS'],
    NOW(),
    NOW()
),
(
    '44444444-4444-4444-4444-444444444444',
    'Infosys',
    'INFY',
    ARRAY['Infosys Ltd'],
    NOW(),
    NOW()
),
(
    '55555555-5555-5555-5555-555555555555',
    'HDFC Bank',
    'HDFCBANK',
    ARRAY['HDFC'],
    NOW(),
    NOW()
);

-- =====================================================
-- HERO MOTOCORP NEWS
-- =====================================================

INSERT INTO news (
    id,
    entity_id,
    title,
    url,
    description,
    published_date,
    sentiment,
    source_name,
    created_at,
    updated_at
)
VALUES
(gen_random_uuid(),'11111111-1111-1111-1111-111111111111','Hero launches new EV scooter','https://example.com/hero-1','New EV scooter announced','2026-05-01','POSITIVE','Economic Times',NOW(),NOW()),
(gen_random_uuid(),'11111111-1111-1111-1111-111111111111','Hero Q4 profit rises','https://example.com/hero-2','Strong quarterly earnings','2026-05-02','POSITIVE','Business Standard',NOW(),NOW()),
(gen_random_uuid(),'11111111-1111-1111-1111-111111111111','Hero expands dealership network','https://example.com/hero-3','Expansion across India','2026-05-03','POSITIVE','Mint',NOW(),NOW()),
(gen_random_uuid(),'11111111-1111-1111-1111-111111111111','Hero stock gains 2 percent','https://example.com/hero-4','Investors react positively','2026-05-04','POSITIVE','CNBC TV18',NOW(),NOW()),
(gen_random_uuid(),'11111111-1111-1111-1111-111111111111','Hero announces dividend','https://example.com/hero-5','Dividend declared for shareholders','2026-05-05','POSITIVE','Moneycontrol',NOW(),NOW());

-- =====================================================
-- RELIANCE NEWS
-- =====================================================

INSERT INTO news (
    id,
    entity_id,
    title,
    url,
    description,
    published_date,
    sentiment,
    source_name,
    created_at,
    updated_at
)
VALUES
(gen_random_uuid(),'22222222-2222-2222-2222-222222222222','Reliance expands retail business','https://example.com/rel-1','Retail footprint increases','2026-05-01','POSITIVE','Economic Times',NOW(),NOW()),
(gen_random_uuid(),'22222222-2222-2222-2222-222222222222','Reliance announces investment plan','https://example.com/rel-2','Capex for next fiscal year','2026-05-02','POSITIVE','Mint',NOW(),NOW()),
(gen_random_uuid(),'22222222-2222-2222-2222-222222222222','Reliance stock stable','https://example.com/rel-3','Markets remain neutral','2026-05-03','NEUTRAL','Business Standard',NOW(),NOW()),
(gen_random_uuid(),'22222222-2222-2222-2222-222222222222','Jio subscriber growth continues','https://example.com/rel-4','Strong telecom performance','2026-05-04','POSITIVE','Moneycontrol',NOW(),NOW()),
(gen_random_uuid(),'22222222-2222-2222-2222-222222222222','Reliance quarterly revenue grows','https://example.com/rel-5','Revenue beats expectations','2026-05-05','POSITIVE','CNBC TV18',NOW(),NOW());

-- =====================================================
-- TCS NEWS
-- =====================================================

INSERT INTO news (
    id,
    entity_id,
    title,
    url,
    description,
    published_date,
    sentiment,
    source_name,
    created_at,
    updated_at
)
VALUES
(gen_random_uuid(),'33333333-3333-3333-3333-333333333333','TCS wins major contract','https://example.com/tcs-1','Large international deal','2026-05-01','POSITIVE','Economic Times',NOW(),NOW()),
(gen_random_uuid(),'33333333-3333-3333-3333-333333333333','TCS hires fresh graduates','https://example.com/tcs-2','Campus hiring initiative','2026-05-02','POSITIVE','Mint',NOW(),NOW()),
(gen_random_uuid(),'33333333-3333-3333-3333-333333333333','TCS Q4 results announced','https://example.com/tcs-3','Revenue and profit update','2026-05-03','NEUTRAL','Business Standard',NOW(),NOW()),
(gen_random_uuid(),'33333333-3333-3333-3333-333333333333','TCS launches AI platform','https://example.com/tcs-4','Enterprise AI offering','2026-05-04','POSITIVE','Moneycontrol',NOW(),NOW()),
(gen_random_uuid(),'33333333-3333-3333-3333-333333333333','TCS shares rise','https://example.com/tcs-5','Positive market sentiment','2026-05-05','POSITIVE','CNBC TV18',NOW(),NOW());

-- =====================================================
-- INFOSYS NEWS
-- =====================================================

INSERT INTO news (
    id,
    entity_id,
    title,
    url,
    description,
    published_date,
    sentiment,
    source_name,
    created_at,
    updated_at
)
VALUES
(gen_random_uuid(),'44444444-4444-4444-4444-444444444444','Infosys launches cloud service','https://example.com/infy-1','New cloud platform','2026-05-01','POSITIVE','Economic Times',NOW(),NOW()),
(gen_random_uuid(),'44444444-4444-4444-4444-444444444444','Infosys signs banking deal','https://example.com/infy-2','Strategic partnership','2026-05-02','POSITIVE','Mint',NOW(),NOW()),
(gen_random_uuid(),'44444444-4444-4444-4444-444444444444','Infosys stock declines slightly','https://example.com/infy-3','Minor correction','2026-05-03','NEGATIVE','Business Standard',NOW(),NOW()),
(gen_random_uuid(),'44444444-4444-4444-4444-444444444444','Infosys expands Europe operations','https://example.com/infy-4','New offices announced','2026-05-04','POSITIVE','Moneycontrol',NOW(),NOW()),
(gen_random_uuid(),'44444444-4444-4444-4444-444444444444','Infosys AI investments increase','https://example.com/infy-5','Focus on GenAI','2026-05-05','POSITIVE','CNBC TV18',NOW(),NOW());

-- =====================================================
-- HDFC BANK NEWS
-- =====================================================

INSERT INTO news (
    id,
    entity_id,
    title,
    url,
    description,
    published_date,
    sentiment,
    source_name,
    created_at,
    updated_at
)
VALUES
(gen_random_uuid(),'55555555-5555-5555-5555-555555555555','HDFC Bank expands branch network','https://example.com/hdfc-1','New branches opened','2026-05-01','POSITIVE','Economic Times',NOW(),NOW()),
(gen_random_uuid(),'55555555-5555-5555-5555-555555555555','HDFC reports strong earnings','https://example.com/hdfc-2','Quarterly results released','2026-05-02','POSITIVE','Mint',NOW(),NOW()),
(gen_random_uuid(),'55555555-5555-5555-5555-555555555555','HDFC digital banking grows','https://example.com/hdfc-3','User adoption rises','2026-05-03','POSITIVE','Business Standard',NOW(),NOW()),
(gen_random_uuid(),'55555555-5555-5555-5555-555555555555','HDFC stock remains stable','https://example.com/hdfc-4','Limited volatility','2026-05-04','NEUTRAL','Moneycontrol',NOW(),NOW()),
(gen_random_uuid(),'55555555-5555-5555-5555-555555555555','HDFC launches SME lending product','https://example.com/hdfc-5','New offering for businesses','2026-05-05','POSITIVE','CNBC TV18',NOW(),NOW());
