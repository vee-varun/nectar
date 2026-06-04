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

