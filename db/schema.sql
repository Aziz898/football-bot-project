-- Таблица матчей
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_home TEXT NOT NULL,
    team_away TEXT NOT NULL,
    start_time TEXT NOT NULL,
    status TEXT DEFAULT 'scheduled',
    score_home INTEGER DEFAULT 0,
    score_away INTEGER DEFAULT 0
);

-- Таблица постов
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    published BOOLEAN DEFAULT 0
);

-- Таблица настроек
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT
);

-- Таблица логов
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT DEFAULT CURRENT_TIMESTAMP,
    level TEXT,
    message TEXT
);
