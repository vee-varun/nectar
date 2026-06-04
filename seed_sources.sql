-- seed_sources.sql

INSERT INTO sources (
    name,
    rss_url,
    website_url,
    source_type,
    is_active,
    fetch_interval_minutes,
    archive_day_range,
    status,
    metadata_json,
    created_at,
    updated_at
)
VALUES
(
    'Times of India - Business',
    'https://timesofindia.indiatimes.com/rssfeeds/1898055.cms',
    'https://timesofindia.indiatimes.com/business',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
),
(
    'Times of India - Technology',
    'https://timesofindia.indiatimes.com/rssfeeds/66949542.cms',
    'https://timesofindia.indiatimes.com/technology',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
),
(
    'Economic Times - Markets',
    'https://economictimes.indiatimes.com/rssfeedsdefault.cms',
    'https://economictimes.indiatimes.com/markets',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
),
(
    'Economic Times - Industry',
    'https://economictimes.indiatimes.com/industry/rssfeeds/13352306.cms',
    'https://economictimes.indiatimes.com/industry',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
),
(
    'Economic Times - Technology',
    'https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms',
    'https://economictimes.indiatimes.com/tech',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
),
(
    'Economic Times - AI',
    'https://economictimes.indiatimes.com/ai/rssfeeds/119215726.cms',
    'https://ai.economictimes.com/',
    'rss',
    TRUE,
    60,
    30,
    'ACTIVE',
    '{}'::jsonb,
    NOW(),
    NOW()
);
